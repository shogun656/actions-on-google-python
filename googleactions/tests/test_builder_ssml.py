from googleactions import SsmlBuilder, InterpretAs, ProsodyRate, ProsodyPitch, EmphasisLevel
from unittest.mock import MagicMock


def setup_module(module):
    module.get_start_tag = SsmlBuilder.get_start_tag
    module.get_end_tag = SsmlBuilder.get_end_tag
    module.get_attributes = SsmlBuilder.get_attributes
    global MODULE
    MODULE = module


def teardown_module(module):
    SsmlBuilder.get_start_tag = module.get_start_tag
    SsmlBuilder.get_end_tag = module.get_end_tag
    SsmlBuilder.get_attributes = module.get_attributes


def test_constants():
    assert SsmlBuilder.SPEAK == 'speak'
    assert SsmlBuilder.BREAK == 'break'
    assert SsmlBuilder.SAY_AS == 'say-as'
    assert SsmlBuilder.AUDIO == 'audio'
    assert SsmlBuilder.DESC == 'desc'
    assert SsmlBuilder.PARAGRAPH == 'p'
    assert SsmlBuilder.SENTENCE == 's'
    assert SsmlBuilder.SUB == 'sub'
    assert SsmlBuilder.PROSODY == 'prosody'
    assert SsmlBuilder.EMPHASIS == 'emphasis'
    assert SsmlBuilder.PAR == 'par'
    assert SsmlBuilder.SEQ == 'seq'
    assert SsmlBuilder.MEDIA == 'media'


def test_init():
    ssml_builder = SsmlBuilder()
    assert ssml_builder


def test_start_tag():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_tag('name')
    assert self.txt == '<name>'


def test_start_tag_attributes():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_tag('name', attributes=[('a', 'b')])
    assert self.txt == '<name a="b">'


def test_start_tag_is_end():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_tag('name', is_end=True)
    assert self.txt == '<name/>'


def test_start_tag_is_end_attributes():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_tag('name', attributes=[('a', 'b')], is_end=True)
    assert self.txt == '<name a="b"/>'


def test_end_tag():
    ssml_builder = SsmlBuilder()
    ssml_builder.get_end_tag = MagicMock(return_value='</name>')
    self = ssml_builder.end_tag('name')
    assert self.txt == '</name>'


def test_do_break():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.do_break(1)
    assert self.txt == '<break time="1s" strength="medium"/>'


def test_say_as():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.say_as('text', interpret_as=InterpretAs.EXPLETIVE)
    assert self.txt == '<say-as interpret-as="expletive">text</say-as>'


def test_say_as_all():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.say_as('1960-09-10', interpret_as=InterpretAs.DATE, as_format='1')
    assert self.txt == '<say-as interpret-as="date" format="1">1960-09-10</say-as>'


def test_desc():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.desc('description')
    assert self.txt == '<desc>description</desc>'


def test_audio():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.audio(src='https://www.example.com/audio.mp3',
                              alt='alt',
                              desc='desc',
                              clip_begin=1,
                              clip_end=2,
                              speed='200%',
                              repeat_count='2',
                              repeat_dur='3s',
                              sound_level='+2dB')
    assert self.txt == '<audio src="https://www.example.com/audio.mp3" clipBegin="1s" clipEnd="2s" speed="200%" ' \
                       'repeatCount="2" repeatDur="3s" soundLevel="+2dB"><desc>desc</desc>alt</audio>'


def test_audio_is_end():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.audio(src='https://www.example.com/audio.mp3')
    assert self.txt == '<audio src="https://www.example.com/audio.mp3"/>'


def test_p():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.p('text')
    assert self.txt == '<p>text</p>'


def test_start_p():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_p()
    assert self.txt == '<p>'


def test_end_p():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_p()
    assert self.txt == '</p>'


def test_s():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.s('text')
    assert self.txt == '<s>text</s>'


def test_start_s():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_s()
    assert self.txt == '<s>'


def test_end_s():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_s()
    assert self.txt == '</s>'


def test_prosody():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.prosody('text', rate=ProsodyRate.X_FAST, pitch=ProsodyPitch.X_HIGH)
    assert self.txt == '<prosody rate="x-fast" pitch="x-high">text</prosody>'


def test_start_prosody():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_prosody(rate=ProsodyRate.X_FAST, pitch=ProsodyPitch.X_HIGH)
    assert self.txt == '<prosody rate="x-fast" pitch="x-high">'


def test_end_prosody():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_prosody()
    assert self.txt == '</prosody>'


def test_emphasis():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.emphasis('text', level=EmphasisLevel.STRONG)
    assert self.txt == '<emphasis level="strong">text</emphasis>'


def test_start_par():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_par()
    assert self.txt == '<par>'


def test_end_par():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_par()
    assert self.txt == '</par>'


def test_start_seq():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_seq()
    assert self.txt == '<seq>'


def test_end_seq():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_seq()
    assert self.txt == '</seq>'


def test_start_media():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.start_media(id='id',
                                    begin='1s',
                                    end='2s',
                                    repeat_count=4,
                                    repeat_dur='10s',
                                    sound_level='+10dB',
                                    fade_in_dur='1s',
                                    fade_out_dur='1s')
    assert self.txt == '<media xml:id="id" begin="1s" end="2s" repeatCount="4" ' \
                       'repeatDur="10s" soundLevel="+10dB" fadeInDur="1s" fadeOutDur="1s">'


def test_end_media():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.end_media()
    assert self.txt == '</media>'


def test_text():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.text('text')
    assert self.txt == 'text'


def test_text_is_none():
    ssml_builder = SsmlBuilder()
    self = ssml_builder.text(None)
    assert self.txt == ''


def test_build():
    ssml_builder = SsmlBuilder()
    txt = ssml_builder.build()
    assert txt == '<speak></speak>'


def test_build():
    ssml_builder = SsmlBuilder()
    ssml_builder.text('text')
    txt = ssml_builder.build()
    assert txt == '<speak>text</speak>'


def test_get_start_tag():
    assert SsmlBuilder.get_start_tag('name', attributes=[('a', 'b')], is_end=False) == '<name a="b">'


def test_get_start_tag_is_end():
    assert SsmlBuilder.get_start_tag('name', attributes=[('a', 'b')], is_end=True) == '<name a="b"/>'


def test_get_attributes():
    assert SsmlBuilder.get_attributes(attributes=[('a', 'b'), ('c', 'd')]) == ' a="b" c="d"'


def test_get_end_tag():
    assert SsmlBuilder.get_end_tag('name') == '</name>'
