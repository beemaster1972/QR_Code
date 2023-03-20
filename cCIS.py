import qrcode as qr
from fpdf import FPDF


class CIS:
    """ Класс определения акцизных марок, в дальнейшем АМ
    параметр numcolumn указывает номер колонки с АМ, если numcolumn меньше нуля, то
    метод get_cis() возвращает всю строку из файла filename"""

    def __init__(self, filename: str, encoding: str = 'utf-8-sig', has_header: bool = True, separator: str = '\t',
                 numcolumn: int = 0):
        self.__filename = filename
        self.__encoding = encoding
        self.__cis = []
        self.__has_header = has_header
        self.__separator = separator
        self.__numcolumn = numcolumn

    def set_filename(self, filename: str):
        self.__filename = filename

    def set_numcolumn(self, numcolumn):
        self.__numcolumn = numcolumn

    def set_separator(self, separator):
        self.__separator = separator

    def get_cis(self):
        """Возвращает список списков содержащих АМ,
        в общем случае вложенные списки из одного элемента вида [['11..'],['22..'],['33..']...]"""
        with open(self.__filename, mode='r', encoding=self.__encoding) as f:
            src_cis = f.readlines()
            self.__cis = [s.strip().split(self.__separator) for s in src_cis[self.__has_header:]]
        if self.__numcolumn >= 0:
            self.__cis = [[km[self.__numcolumn]] for km in self.__cis]
        return self.__cis


class PDF:
    """ Класс для создания pdf """
    def __init__(self, filename: str, format: str = 'A4', unit: str = 'mm', orientation: str = 'Landscape'):
        self.__filename = filename
        self.__format = format
        self.__unit = unit
        self.__orientation = orientation
        self.__pdf = FPDF(orientation=self.__orientation, format=self.__format, unit=self.__unit)
        self.__pdf.set_font('helvetica', size=10)

    def fill_pages(self, contents: list, footer: str, width: (float, int) = 10, height: (float, int) = 10,
                   gap: (float, int) = 1, column: int = 0, silent: bool = False):
        """Заполнение страниц pdf файла содержимым contents"""
        if type(contents) != list:
            raise ValueError('Тип содержимого должен быть списком')
        elif not len(contents):
            raise ValueError('Пустое содержимое')
        lst = type(contents[0]) == list
        self.__pdf.add_page()
        x, y, count_of_codes = 1, 1, 0
        page_num = 1
        for ind, cis in enumerate(contents):
            cis = cis[column] if lst else cis
            if not silent:
                print('Генерирую -->', ind, cis)
            img = qr.make(cis)
            self.__pdf.image(img.get_image(), x, y, w=width, h=height)
            count_of_codes += 1
            x = x + width + gap if x <= self.__pdf.epw - width else 0
            y = y + height + gap if x == 0 else y
            if y > (self.__pdf.eph + 30 - height):
                x, y = self.__pdf.epw / 2, self.__pdf.eph + 30 - 1
                self.__pdf.text(x, y, footer + 'page ' + str(page_num) + ' total codes on page ' + str(count_of_codes))
                page_num += 1
                self.__pdf.add_page()
                x, y, count_of_codes = 1, 1, 0
        self.__pdf.text(self.__pdf.epw / 2, self.__pdf.eph + 30 - 1,
                        footer + 'page ' + str(page_num) + ' total codes on page ' + str(count_of_codes))
        self.__pdf.output(self.__filename)
