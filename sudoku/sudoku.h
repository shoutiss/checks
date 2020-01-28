// Compile-time options for the game of Sudoku.

// Game's author
#define AUTHOR "Mr. Shoutis"

// Game's title
#define TITLE "Sudoku"

// Banner's colors
#define FG_BANNER COLOR_RED
#define BG_BANNER COLOR_BLACK

// Grid's colors
#define FG_GRID COLOR_BLUE
#define BG_GRID COLOR_BLACK

// Border's colors
#define FG_BORDER COLOR_WHITE
#define BG_BORDER COLOR_CYAN

// Logo's colors
#define FG_LOGO COLOR_WHITE
#define BG_LOGO COLOR_BLACK

// User entered digits's colors
#define FG_DIGITS COLOR_MAGENTA
#define BG_DIGITS COLOR_BLACK

// Original digit's colors
#define FG_ORIGINAL COLOR_CYAN
#define BG_ORIGINAL COLOR_BLACK

// Nicknames for pairs of colors
enum { PAIR_BANNER = 1, PAIR_GRID, PAIR_BORDER, PAIR_LOGO, PAIR_DIGITS, PAIR_ORIGINAL };
