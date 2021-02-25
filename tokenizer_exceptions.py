from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...symbols import ORTH, NORM
from ...util import update_exc

_exc = {}

for token in ["᾽Απ'", "᾽ΑΠ'", "ἀφ'", "᾽Αφ", "ἀπὸ"]:
    _exc[token] = [{ORTH: token, NORM: "από"}]

for token in ["᾽Αλλ'", "ἀλλ'", "ἀλλὰ"]:
    _exc[token] = [{ORTH: token, NORM: "ἀλλά"}]

for token in ["παρ'", "Παρ'", "παρὰ", "παρ"]:
    _exc[token] = [{ORTH: token, NORM: "παρά"}]

for token in ["καθ'", "Καθ'","κατ'", "Κατ'", "κατὰ"]:
    _exc[token] = [{ORTH: token, NORM: "κατά"}]

for token in ["Ἐπ'", "ἐπ'", "ἐπὶ","Εφ'","εφ'"]:
    _exc[token] = [{ORTH: token, NORM: "επί"}]

for token in ["Δι'", "δι'", "διὰ"]:
    _exc[token] = [{ORTH: token, NORM: "διά"}]

for token in ["Ὑπ'", "ὑπ'","ὑφ'" ]:
    _exc[token] = [{ORTH: token, NORM: "ὑπό"}]

for token in ["Μετ'", "μετ'", "μεθ'", "μετὰ"]:
    _exc[token] = [{ORTH: token, NORM: "μετά"}]

for token in ["Μ'", "μ'", "μέ", "μὲ"]:
    _exc[token] = [{ORTH: token, NORM: "με"}]

for token in ["Σ'", "σ'", "σέ", "σὲ"]:
    _exc[token] = [{ORTH: token, NORM: "σε"}]

for token in ["Τ'", "τ'", "τέ", "τὲ"]:
    _exc[token] = [{ORTH: token, NORM: "τε"}]

for token in ["Δ'", "δ'", "δὲ"]:
    _exc[token] = [{ORTH: token, NORM: "δέ"}]


_other_exc = {
    "ʼ": [{ORTH: "ʼ", NORM: "'"}],
    "τὴν": [{ORTH: "τὴν", NORM: "τήν"}],
    "τὸν": [{ORTH: "τὸν", NORM: "τόν"}],
    "κἀγὼ": [{ORTH: "κἀγὼ", NORM: "ἐγώ"}],
    "καὶ": [{ORTH: "καὶ", NORM: "καί"}],
    "μὲν": [{ORTH: "μὲν", NORM: "μέν"}],
    "μὴν": [{ORTH: "μὴν", NORM: "μήν"}],

}

_exc.update(_other_exc)

_exc_data = {}

_exc.update(_exc_data)

TOKENIZER_EXCEPTIONS = update_exc(BASE_EXCEPTIONS, _exc)
