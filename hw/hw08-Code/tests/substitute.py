test = {
  'name': 'substitute',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (substitute '((b . e) (d . f)) '(a (a b c) d))
          (a (a e c) f)
          scm> (substitute '((a . b) (c . d)) '(a a b c d))
          (b b b d d)
          scm> (substitute '((a . b) (c . d)) '(a a c d (a b c d)))
          (b b d d (b b d d))
          scm> (substitute '((a . b) (b . c)) '(a b c))
          (b c c)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
