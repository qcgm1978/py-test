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

it(`Assigning Multiple Values At Once`, () => {
  const v = ["a", 2, true];
  const [a, b, c] = v;
  expect(a).toBe("a");
  expect(b).toBe(2);
  expect(c).toBe(true);
  const getConsecutive = num => Array.from(Array(num), (_, i) => i);
  const range = getConsecutive(7);
  const [
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY
  ] = range;
  expect(MONDAY).toBe(0);
  expect(TUESDAY).toBe(1);
  expect(SUNDAY).toBe(6);
});

it(`A set is an unordered “bag” of unique values. JS: The Set object lets you store unique values of any type, whether primitive values or object references  `, () => {
  let a_set = new Set([1]);
  expect(a_set).toEqual(new Set([1]));
  expect(a_set).toBeInstanceOf(Set);
  a_set = new Set([1, 2]);
  expect(a_set).toEqual(new Set([1, 2]));
  // a_set = new Set([1, 2, { a: 1 }]);
});
