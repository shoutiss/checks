# Compiler to use
CC = clang

# Flags to pass compiler
CFLAGS = -fsanitize=signed-integer-overflow -fsanitize=undefined -ggdb3 -O0 -Qunused-arguments -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wshadow
# clang -ggdb3 -O0 -std=c11 -Wall -Werror -Wextra -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wshadow
# Name for executable
EXE = sort

# Space-separated list of header files
HDRS = bubble.h

# Space-separated list of libraries, if any,
# Each of which should be prefixed with -l
LIBS = -lcs50 -lcrypt

# Space-separated list of source files
SRCS = sort.c bubble.c

# Automatically generated list of object files
#OBJS = $(SRCS:.c=.o)


# Default target
$(EXE): $(OBJS) $(HDRS) Makefile
	$(CC) $(CFLAGS) -o $@ $(SRCS) $(LIBS)

# Dependencies
$(OBJS): $(HDRS) Makefile

# Housekeeping
clean:
	rm -f core $(EXE) *.o
