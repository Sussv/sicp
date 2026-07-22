test = {
  'name': 'midterm_distribution',
  'points': 100,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> select * from midterm_distribution;
          90.0|7
          80.0|8
          70.0|7
          60.0|25
          50.0|39
          40.0|20
          30.0|9
          20.0|1
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
