# VSCode italic font settings

*Add this to settings.json (`cmd ,`):*

```json
{
  "editor.fontFamily": "Operator Mono, Fira Code iScript, Menlo, Monaco, 'Courier New', monospace",
  "editor.fontLigatures": true,
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": [
          //following will be in italic
          "comment",
          "entity.name.type.class", //class names
          "constant", //String, Number, Boolean…, this, super
          "storage.modifier", //static keyword
          "storage.type.class.js", //class keyword
          "keyword", //import, export, return…
        ],
        "settings": {
          "fontStyle": "italic"
        }
      },
      {
        "scope": [
          //following will be excluded from italics (VSCode has some defaults for italics)

          "invalid",
          "keyword.operator",
          "constant.numeric.css",
          "keyword.other.unit.px.css",
          "constant.numeric.decimal.js",
          "constant.numeric.json"
        ],
        "settings": {
          "fontStyle": ""
        }
      }
    ]
  },
}
```

## Resources

[cufofonts](https://www.cufonfonts.com/font/operator-mono)
[firacodeiscript](https://github.com/kencrocken/FiraCodeiScript)
[firacode](https://github.com/tonsky/FiraCode)

```json
"editor.fontFamily": "Fira Code",
"editor.fontLigatures": true
```

[FiraFlott](https://github.com/kosimst/FiraFlott)