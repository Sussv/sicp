test = {
  'name': 'enumerate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (enumerate '(a b c))
          ((0 . a) (1 . b) (2 . c))
          scm> (enumerate '(x y))
          ((0 . x) (1 . y))
          scm> (enumerate '())
          ()
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
