cp TEST_DIR/test.py BASE_DIR/
cp TEST_DIR/input.txt BASE_DIR/
cd BASE_DIR

if grep -q "while" prep19.py; then
  echo "Don't use a while loop!"
fi

if ! grep -q "for" prep19.py; then
  echo "Use a for loop!"
fi

cat input.txt | python3 -u test.py
