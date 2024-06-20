EXECUTABLE="./check_all_ciphers Piccolo128 bitslice16 -samples=32"
ITERATIONS=50000

# parameters for all the variations
# LED64 table
# LED64 vperm
# LED64 bitslice32
# LED128 table
# LED128 vperm
# LED128 bitslice32

# PRESENT80 table
# PRESENT80 vperm
# PRESENT80 bitslice16
# PRESENT128 table
# PRESENT128 vperm
# PRESENT128 bitslice16

# Piccolo80 table
# Piccolo80 vperm
# Piccolo80 bitslice16
# Piccolo128 table
# Piccolo128 vperm 
# Piccolo128 bitslice16

cd bin
for ((i = 1; i <= ITERATIONS; i++)); do
    echo "Running iteration $i"  
    $EXECUTABLE  
done
# save the performace data into relevant file
mv perf_data.txt piccolo128bitslice_perf.csv
