it(`__dirname`, () => {
    expect(__dirname).toBe("/Users/zhanghongliang/Documents/py-test/__test__")
    // expect(process.cwd()).toBe("/Applications")
    // process.chdir('/')
    // expect(__dirname).toBe("/Users/zhanghongliang/Documents/py-test/__test__")
    // expect(process.cwd()).toBe("/Applications")
});
it(`__filename`, () => {
    expect(__filename).toBe('/Users/zhanghongliang/Documents/py-test/__test__/comprehensions.spec.js')
    const filename = __filename.split('/').pop()
    expect(filename).toBe('comprehensions.spec.js')
    const [shortname, extension] = /(.+)(\..+?)$/.exec(filename).slice(1)
    expect(shortname).toBe('comprehensions.spec')
    expect(extension).toBe('.js')
});
it(`glob`, done => {
    expect(process.env.PWD).toBe("/Users/zhanghongliang/Documents/py-test")
    const fs = require('fs');

    const files = fs.readdirSync(process.env.PWD + '/.vscode/', { withFileTypes: true })
        .filter(item => !item.isDirectory())
        .map(item => item.name)
    expect(files).toEqual(['launch.json', 'settings.json'])
    var glob = require("glob")

    // options is optional
    glob(".vscode/*.json", function (er, files) {
        // files is an array of filenames.
        // If the `nonull` option is set, and nothing
        // was found, then files is ["**/*.js"]
        // er is an error object or null.
        expect(files.map(item => item.split('/').pop())).toEqual(['launch.json', 'settings.json']);
        done()
    })
});