from googleactions import TableCardBuilder, HorizontalAlignment, Button, Image


def test_init():
    table_card_builder = TableCardBuilder()
    assert table_card_builder.tc_rows == []
    assert table_card_builder.tc_divs == []
    assert table_card_builder.tc_headers == []
    assert table_card_builder.tc_aligns == []
    assert table_card_builder.tc_button is None
    assert table_card_builder.tc_title is None
    assert table_card_builder.tc_subtitle is None
    assert table_card_builder.tc_image is None


def test_title():
    table_card_builder = TableCardBuilder()
    self = table_card_builder.title('title')
    assert self.tc_title == 'title'


def test_subtitle():
    table_card_builder = TableCardBuilder()
    self = table_card_builder.subtitle('subtitle')
    assert self.tc_subtitle == 'subtitle'


def test_row():
    table_card_builder = TableCardBuilder()
    self = table_card_builder.row(['col1', 'col2'], divider_after=True)
    assert self.tc_rows == [['col1', 'col2']]
    assert self.tc_divs == [True]


def test_headers():
    table_card_builder = TableCardBuilder()
    self = table_card_builder.headers(['header1', 'header2'])
    assert self.tc_headers == ['header1', 'header2']
    assert self.tc_aligns == [HorizontalAlignment.CENTER, HorizontalAlignment.CENTER]


def test_headers_align():
    table_card_builder = TableCardBuilder()
    self = table_card_builder.headers(['header1', 'header2'], aligns=[HorizontalAlignment.LEADING,
                                                                      HorizontalAlignment.TRAILING])
    assert self.tc_headers == ['header1', 'header2']
    assert self.tc_aligns == [HorizontalAlignment.LEADING, HorizontalAlignment.TRAILING]


def test_button():
    table_card_builder = TableCardBuilder()
    button = Button(title='title', url='url')
    self = table_card_builder.button(button)
    assert self.tc_button == button


def test_image():
    table_card_builder = TableCardBuilder()
    image = Image(url='url', alt='alt')
    self = table_card_builder.image(image)
    assert self.tc_image == image


def test_build():
    table_card_builder = TableCardBuilder()
    button = Button(title='title', url='url')
    image = Image(url='url', alt='alt')
    cells = ['col1', 'col2', 'col3']
    headers = ['header1', 'header2', 'header3']
    table_card = (table_card_builder.title(title='Title')
                                    .subtitle(subtitle='Subtitle')
                                    .row(cells=cells)
                                    .headers(headers=headers)
                                    .button(button=button)
                                    .image(image=image)
                                    .build())
    assert table_card.title == 'Title'
    assert table_card.subtitle == 'Subtitle'
    assert table_card.image == image
    assert table_card.buttons == [button]
    for index, c_prop in enumerate(table_card.column_properties):
        assert c_prop.header == headers[index]
        assert c_prop.horizontal_alignment == HorizontalAlignment.CENTER
    for index, row in enumerate(table_card.rows):
        cells = row.cells
        assert cells[0].text == 'col1'
        assert cells[1].text == 'col2'
        assert cells[2].text == 'col3'
        assert row.divider_after is False
