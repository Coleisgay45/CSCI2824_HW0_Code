#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD
 class Exam:
    def PassFail(self, exam1, exam2, exam3, exam4):
      final = exam1 + exam2 + exam3 + exam4
      test = 600 * 0.55
      final = test - final
      return int(final)
