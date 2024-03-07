
it('should calculate the monthly rate correctly', function () {
  // ...
  const values1 = {
    amount: 10000,
    years: 5,
    rate: 5,
  };
  expect(calculateMonthlyPayment(values1)).toEqual("188.71");
});


it("should return a result with 2 decimal places", function() {
  // ..
  const values2 = {
    amount: 10043,
    years: 8,
    rate: 5.8,
  };
  expect(calculateMonthlyPayment(values2)).toEqual("131.00");
});

/// etc
