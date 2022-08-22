cp TEST_DIR/test.py BASE_DIR/
cp TEST_DIR/input.txt BASE_DIR/
cd BASE_DIR

cat input.txt | python3 -u test.py
