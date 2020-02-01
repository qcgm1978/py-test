it(`__dirname`, () => {
    expect(__dirname).toBe("/Users/zhanghongliang/Documents/py-test/__test__")
    process.chdir('/Applications')
    expect(__dirname).toBe("/Users/zhanghongliang/Documents/py-test/__test__")
    expect(process.cwd()).toBe("/Applications")
});