import os
num_runs = 5
run_list = ["bc","bfs","cc","cc_sv","pr","pr_spmv","sssp","tc"] 

os.system("rm *.log && rm *.stats")

for benchmark in run_list:
    os.system("perf record -e br_misp_retired.all_branches:ppp,br_misp_retired.cond:ppp,br_inst_retired.cond:ppp,br_inst_retired.all_branches:ppp -j any,u -o perf.data -- ./{0} -g24 -n10".format(benchmark))
    os.system("perf script -i perf.data > perf_script.txt")
    os.system("python3 UpperBound.py --filter-file={0}.cc".format(benchmark))