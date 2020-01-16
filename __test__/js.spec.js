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

it(`search list(array)`, () => {
  const a_list = ["a", "b", "new", "mpilgrim", "new"];
  expect(a_list.indexOf("new")).toBe(2);
  expect("new" in a_list).toBeFalsy();
  expect(a_list.indexOf("new")).not.toBe(-1);
  expect(a_list.indexOf("c")).toBe(-1);
});

it(`remote list(array) items`, () => {
  let a_list = ["a", "b", "new", "mpilgrim", "new"];
  delete a_list[1];
  expect(a_list)
    .toEqual(["a", undefined, "new", "mpilgrim", "new"])
    .toEqual(["a", , "new", "mpilgrim", "new"]);
  a_list = ["a", "b", "new", "mpilgrim", "new"];
  a_list.splice(1, 1);
  expect(a_list).toEqual(["a", "new", "mpilgrim", "new"]);
  a_list = ["a", "b", "new", "mpilgrim", "new"];
  const index = a_list.indexOf("new");
  a_list.splice(index, 1);
  expect(a_list).toEqual(["a", "b", "mpilgrim", "new"]);
  a_list = ["a", "b", "new", "mpilgrim", "new"];
  expect(a_list.pop()).toBe("new");
  expect(a_list).toEqual(["a", "b", "new", "mpilgrim"]);
  expect(a_list.pop()).toBe("mpilgrim");
});

it(`list(array) in a Boolean context`, () => {
  expect([]).toBeTruthy();
});

it(`Set`, () => {
  let a_set = new Set([1, 2]);
  expect(a_set).toEqual(new Set([1, 2]));
  a_set = new Set([1, 2, { a: 1 }]);
  expect(a_set).toEqual(new Set([1, 2, { a: 1 }]));
  expect(a_set).toStrictEqual(new Set([1, 2, { a: 1 }]));
  expect(a_set == new Set([1, 2, { a: 1 }])).toBeFalsy();
  const obj = {};
  expect(obj).toEqual({});
  expect(obj).toStrictEqual({});
  expect(obj == {}).toBeFalsy();
  class Parent {
    constructor() {
      this.obj = 1;
    }
  }
  const child = new Parent();
  expect(child)
    .toEqual({ obj: 1 })
    .not.toStrictEqual({ obj: 1 });
  expect(child).toBeInstanceOf(Parent);
  expect({ obj: 1 }).not.toBeInstanceOf(Parent);
});
