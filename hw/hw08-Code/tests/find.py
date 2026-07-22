test = {
  'name': 'find',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (find (lambda (x) (> x 3)) '(1 2 3 4 5))
          4
          scm> (find (lambda (x) (> x 100)) '(1 2 3 4 5))
          #f
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
