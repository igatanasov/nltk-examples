#!/usr/bin/python
# Analyzing meaning of sentences

from __future__ import division
import nltk
from nltk import load_parser
import re


def english_to_sql():
    nltk.data.show_cfg("grammars/book_grammars/sql0.fcfg")

    cp = load_parser("grammars/book_grammars/sql0.fcfg", trace=3)
    query = "What cities are located in China"
    trees = cp.parse(query.split())
    answer = list(trees)[0].label()['SEM']
    q = " ".join(answer)
    print(q)
    from nltk.sem import chat80
    rows = chat80.sql_query('corpora/city_database/city.db', q)
    for r in rows:
        print(
            r[0], )


def logic_parser():
    lp = nltk.sem.Expression.fromstring
    SnF = lp('SnF')
    NotFnS = lp('-FnS')
    R = lp('SnF -> -FnS')

    val = nltk.Valuation([('P', True), ('Q', True), ('R', False)])
    dom = set([])
    g = nltk.Assignment(dom)
    m = nltk.Model(dom, val)
    print("eval(P&Q)=", m.evaluate('(P & Q)', g))
    print("eval -(P&Q)=", m.evaluate('-(P & Q)', g))
    print("eval(P&R)=", m.evaluate('(P & R)', g))
    print("eval(-(P|R))=", m.evaluate('-(P | R)', g))


def first_order_logic():
    tlp = nltk.sem.Expression.fromstring
    sig = {"walk": "<e,t>"}
    parsed = tlp("walk(angus)", sig)
    print("parsed_arg(value,type)=", parsed.argument, parsed.argument.type)
    print("parsed_func(value,type)=", parsed.function, parsed.function.type)


def truth_model():
    domain = set(['b', 'o', 'c'])
    v = """
  bertie => b
  olive => o
  cyril => c
  boy => {b}
  girl => {o}
  dog => {c}
  walk => {o, c}
  see => {(b,o), (c,b), (o,c)}
  """
    val = nltk.Valuation.fromstring(v)
    print(val)
    print(('o', 'c') in val["see"])
    print(('b', ) in val["boy"])
    g = nltk.Assignment(domain, [('x', 'o'), ('y', 'c')])
    model = nltk.Model(domain, val)
    print("model.evaluate=", model.evaluate("see(olive,y)", g))


def main():
    # english_to_sql()
    # logic_parser()
    # first_order_logic()
    truth_model()


if __name__ == "__main__":
    main()
