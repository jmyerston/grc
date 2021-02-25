from typing import Optional
from thinc.api import Model

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
from .lex_attrs import LEX_ATTRS
from .punctuation import TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES, TOKENIZER_INFIXES
#from .lemmatizer import AncientGreekLemmatizer
from ...language import Language



class AncientGreekDefaults(Language.Defaults):
    tokenizer_exceptions = TOKENIZER_EXCEPTIONS
    prefixes = TOKENIZER_PREFIXES
    suffixes = TOKENIZER_SUFFIXES
    infixes = TOKENIZER_INFIXES
    lex_attr_getters = LEX_ATTRS
    stop_words = STOP_WORDS


class AncientGreek(Language):
    lang = "grc"
    Defaults = AncientGreekDefaults

#@AncientGreek.factory(
#    "lemmatizer",
#    assigns=["token.lemma"],
#    default_config={"model": None, "mode": "pos_lookup"},
#    default_score_weights={"lemma_acc": 1.0},
#)

def make_lemmatizer(nlp: Language, model: Optional[Model], name: str, mode: str):
    return AncientGreekLemmatizer(nlp.vocab, model, name, mode=mode)


__all__ = ["AncientGreek"]
