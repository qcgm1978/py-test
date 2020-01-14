it(`list(array) slice`, () => {
  let a_list = ["a", 2.0, 3, true];
  a_list.push("four", "Ω");
  expect(a_list).toEqual(["a", 2.0, 3, true, "four", "Ω"]);
  a_list.unshift("Ω");
  expect(a_list).toEqual(["Ω", "a", 2.0, 3, true, "four", "Ω"]);
});
it(`push`, () => {
  let a_list = ["a", "b", "c"];
  a_list.push("d", "e", "f");
  expect(a_list).toEqual(["a", "b", "c", "d", "e", "f"]);
  a_list = ["a", "b", "c"];
  a_list.push(["d", "e", "f"]);
  expect(a_list).toEqual(["a", "b", "c", ["d", "e", "f"]]);
  expect(a_list.length).toBe(4);
  expect(a_list[a_list.length - 1]).toEqual(["d", "e", "f"]);
});
