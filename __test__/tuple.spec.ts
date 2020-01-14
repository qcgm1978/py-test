it(`Tuple`, () => {
  var a_tuple: [any, string, string, string, string] = [
    "a",
    "b",
    "mpilgrim",
    "z",
    "example"
  ];
  expect(a_tuple).toEqual(["a", "b", "mpilgrim", "z", "example"]);
  expect(a_tuple[0]).toEqual("a");
  expect(a_tuple[a_tuple.length - 1]).toEqual("example");
  expect(a_tuple.slice(1, 3)).toEqual(["b", "mpilgrim"]);
  a_tuple.push(2, "Bill");
  expect(a_tuple).toEqual(["a", "b", "mpilgrim", "z", "example", 2, "Bill"]);
  a_tuple.pop();
  expect(a_tuple).toEqual(["a", "b", "mpilgrim", "z", "example", 2]);
  var b_tuple: [any] = [null];
  expect(b_tuple).toBeTruthy();
  var c_tuple: [Boolean] = [false];
  expect(c_tuple).toBeTruthy();
});
