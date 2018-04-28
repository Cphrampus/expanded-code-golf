#include<stdio.h>
#include<string.h>

// original
// char *a,b[10],*i,*o;f(x,y){*b=*a;for(x=1;x<8;b[x++]=a[y=index(i,o[x])-i],b[x++]=a[y+1]);}

/* char *a, b[10], *i, *o; */

// making it a function
/*void color_swap(){
	int x;
	int y;

	*b=*a;

	for (x=1;x<8;b[x++]=a[y=index(i,o[x])-i],b[x++]=a[y+1]);

}*/

// that isn't much better, let's rename the globals
char *color, buffer[10], *from, *to;

/*void color_swap(){
	int x;
	int y;

	*buffer=*color;

	for (x=1;x<8;buffer[x++]=color[y=index(from,to[x])-from],buffer[x++]=color[y+1]);

}*/

// that's a little better, but let's move the actions from the loop header to the body

/*void color_swap(){
	int x;
	int y;

	*buffer=*color;

	for (x=1;x<8;) {
		buffer[x++]=color[y=index(from,to[x])-from];
		buffer[x++]=color[y+1];
	}

}*/

// definitely easier to read now without that comma expression and with more space, but we can do more still

/*void color_swap(){
	int x;
	int y;

	// copy over the '#'
	*buffer=*color;

	for (x=1;x<8;) {
		y=index(from,to[x])-from;
		buffer[x++]=color[y];
		buffer[x++]=color[y+1];
	}

}*/

// we can see a bit more clearly where x and y are used, so now we can move those

/*void color_swap(){
	// copy over the '#'
	*buffer=*color;

	for (int x = 1; x<8;) {
		// get the starting index of the character we want
		int y = index(from, to[x])-from;

		// get the first character
		buffer[x++] = color[y];

		// get the second character
		buffer[x++] = color[y+1];
	}
}*/

// with those comments it is almost pretty readable! But we can clean it up a little more

void color_swap(){
	// copy over the '#'
	*buffer=*color;

	for (int x = 1; x<8;) {
		// get the starting index of the character we want
		int position = index(from, to[x])-from;

		// get the first character
		buffer[x++] = color[position];

		// get the second character
		buffer[x++] = color[position+1];
	}
}

// testing code
void g() {
	printf("%s %s %s -> ", color, from, to);
	color_swap();
	printf("%s\n", buffer);
}

int main() {
	color="#12345678"; from="#RRGGBBAA"; to="#AARRGGBB";
	g();

	color="#1A2B3C4D"; from="#RRGGBBAA"; to="#AABBGGRR";
	g();

	color="#DEADBEEF"; from="#AARRGGBB"; to="#GGBBAARR";
	g();

	return 0;

	/*
#12345678, #RRGGBBAA, #AARRGGBB -> #78123456
#1A2B3C4D, #RRGGBBAA, #AABBGGRR -> #4D3C2B1A
#DEADBEEF, #AARRGGBB, #GGBBAARR -> #BEEFDEAD
*/
}
