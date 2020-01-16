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

it(`The Set object lets you store unique values of any type`, () => {
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
  expect(typeof child)
    .toBe(typeof { obj: 1 })
    .toBe("object");
});

it(`Py: There are two different ways to add values to an existing set: the add() method, and the update() method.`, () => {
  let a_set = new Set([1, 2]);
  a_set.add(4);
  expect(a_set).toEqual(new Set([1, 2, 4]));
  expect(a_set.size).toBe(3);
  a_set.add(2);
  expect(a_set).toEqual(new Set([1, 2, 4]));
  a_set.add([2, 4, 6]);
  expect(a_set).toEqual(new Set([1, 2, 4, [2, 4, 6]]));
  a_set = new Set([1, 2, 4]);
  [2, 4, 6].map(item => a_set.add(item));
  expect(a_set)
    .toEqual(new Set([1, 2, 4, 6]))
    .toEqual(new Set([2, 1, 4, 6]));
  expect(a_set)
    .toBeInstanceOf(Set)
    .toBeInstanceOf(Object)
    .not.toBeInstanceOf(Function);
  expect(Set.prototype)
    .toBeInstanceOf(Object)
    .toHaveProperty("add")
    .not.toHaveProperty("update");
  Set.prototype.update = function() {
    Array.from(arguments).map(item => {
      if (item instanceof Array) {
        item.map(it => this.add(it));
      } else {
        this.add(item);
      }
    });
  };
  expect(a_set.update).toBeInstanceOf(Function);
  a_set = new Set([1, 2]);
  a_set.update([2, 1, 3, 4]);
  expect(a_set).toEqual(new Set([4, 3, 2, 1]));
  a_set = new Set([1, 2]);
  a_set.update([2, 1], [3, 4]);
  expect(a_set).toEqual(new Set([4, 3, 2, 1]));
});
