test = {
  'name': 'correlation',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT ai_q1_correlation FROM correlation;
          -0.019914779086777017
          sqlite> SELECT ai_q2_correlation FROM correlation;
          -0.017173943785694534
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read lab10.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
