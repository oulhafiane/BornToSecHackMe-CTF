var fs = require("fs");
var text = fs.readFileSync("temp.txt", "utf-8");


var values = [];

const anon_matches = text.match(
  /char[\s]+?(getme[0-9]+)\(\) {\n+(\/\/file[0-9]+)\s+?/g
);

const known_returns = text.match(
  /char[\s]+?(getme[0-9]+)\(\)[ ]?{?\nreturn[ ]+'[a-zA-z]+';/g
);


known_returns.forEach((element) => {
  const match = element.match(
    /char[ ]+getme([0-9]+)\(\) ?{?\s+return[ ]+?'([a-zA-Z]+)'/
  );

  values.push({
    getmeX: match[1],
    fileX: 'none',
    value: match[2],
  });
});

anon_matches.forEach((element) => {
  const match = element.match(/getme([0-9]+).*\n\/\/file([0-9]+)/);

  values.push({
    getmeX: match[1],
    fileX: match[2],
    value: undefined,
  });
});

values.sort((a, b) => {
  return a.getmeX - b.getmeX;
});

values.forEach((val) => {
  const file_nb = parseInt(val.fileX) + 1;
  const getme_nb = parseInt(val.getmeX) - 1;
  const reg = new RegExp(`return\\s+?'[a-zA-Z]';\n+?\/\/file${file_nb}`, "g");
  const anon_returns = text.match(reg);

  if (anon_returns) {
    const res = anon_returns[0].match(/'([a-zA-Z]+)'/);
    values[getme_nb].value = res[1];
  }
});

console.log(values);

const password = values.map(ele=>{
    return ele.value
})

console.log(`the password is : ${password.join('')}`);
