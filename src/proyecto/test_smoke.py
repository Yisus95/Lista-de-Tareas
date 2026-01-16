cat > src/proyecto/test_smoke.py <<'EOF'
def test_smoke():
    assert True
EOF

git add src/proyecto/test_smoke.py
git commit -m "CI: add smoke test to verify pytest discovery"
git push origin chore/rename-folders-cleanup
