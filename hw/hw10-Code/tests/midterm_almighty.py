test = {
  'name': 'midterm_almighty',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from midterm_almighty;
          103.0
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
