# See LICENSE.txt for license details.

CXX = ~/llvm-cfmse/bin/clang++
CXX_FLAGS += -std=c++11 -Wall -fno-exceptions -fno-unwind-tables
OPT = ~/llvm-cfmse/bin/opt
OPT_FLAGS += -S
#PAR_FLAG = -fopenmp

ifneq (,$(findstring icpc,$(CXX)))
	PAR_FLAG = -openmp
endif

ifneq (,$(findstring sunCC,$(CXX)))
	CXX_FLAGS = -std=c++11 -xO3 -m64 -xtarget=native
	PAR_FLAG = -xopenmp
endif

ifneq ($(SERIAL), 1)
	CXX_FLAGS += $(PAR_FLAG)
endif

KERNELS = bc bfs cc cc_sv pr pr_spmv sssp tc
SUITE = $(KERNELS) converter

.PHONY: all
all: $(SUITE)

% : src/%.cc src/*.h
	$(CXX) -g -O2 -mllvm -enable-cfmse=0 $(CXX_FLAGS) $< -o $@

# Testing
include test/test.mk

# Benchmark Automation
include benchmark/bench.mk


.PHONY: clean
clean:
	rm -f $(SUITE) test/out/*
	rm -f *.ll
	rm -f *merged

clean_build:
	rm -f *.ll
