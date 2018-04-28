// the original solution
f=(C,F,T)=>T.replace(/\w/g,(x,i)=>C[F.search(x)-~i%2]);

// let's expand on that

// make it a function so we can more easily make it longer

function color_swap(C,F,T) {
	return T.replace(/\w/g,(x,i)=>C[F.search(x)-~i%2]);
}

// let's make our variables better names, so we can see what's going on

function color_swap(Color, From_Pattern, To_Pattern){
	return To_Pattern.replace(/\w/g,(x,i)=>Color[From_Pattern.search(x)-~i%2]);
}

// a bit better, but let's get those other lambda variables expanded,
// so we can break it all out more

function color_swap(Color, From_Pattern, To_Pattern){
	return To_Pattern.replace(/\w/g, (letter, index)=>Color[From_Pattern.search(letter)-~index%2]);
}

// let's store some intermediate values

function color_swap(Color, From_Pattern, To_Pattern){
	return To_Pattern.replace(/\w/g, (letter, index) => {
		var location = From_Pattern.search(letter);
		var offset = -~index%2;

		return Color[location+offset];
	});
}

// ok, so it's broken out, but could be a bit clearer

function color_swap(Color, From_Pattern, To_Pattern){
	return To_Pattern.replace(/\w/g, (letter, index) => {
		var location = From_Pattern.search(letter);
		var offset = index%2 === 0 ? 1 : 0;

		return Color[location+offset];
	});
}

// that's not too bad, let's add some general comments and wrap it up

function color_swap(Color, From_Pattern, To_Pattern){

	// replace each letter of the To_Pattern string
	return To_Pattern.replace(/\w/g,
		// get the letter we are replacing and the index in the string
		(letter, index) => {
			// find the first instance of the letter we want
			var location = From_Pattern.search(letter);

			// determine whether it is the first or second instance of the number
			// and give the appropriate offset value
			// NOTE: The indexes start at one, because of the leading #
			var offset = index%2 === 0 ? 1 : 0;

			// get the item from the color string to use as replacement
			return Color[location+offset];
		});
}

// tests
console.log(f('#12345678', '#RRGGBBAA', '#AARRGGBB')); // #78123456
console.log(f('#1A2B3C4D', '#RRGGBBAA', '#AABBGGRR')); // #4D3C2B1A
console.log(f('#DEADBEEF', '#AARRGGBB', '#GGBBAARR')); // #BEEFDEAD

console.log(color_swap('#12345678', '#RRGGBBAA', '#AARRGGBB')); // #78123456
console.log(color_swap('#1A2B3C4D', '#RRGGBBAA', '#AABBGGRR')); // #4D3C2B1A
console.log(color_swap('#DEADBEEF', '#AARRGGBB', '#GGBBAARR')); // #BEEFDEAD
