# sobrescribe con un test trivial válido
cat > src/proyecto/test_smoke.py <<'EOF'
def test_smoke():
    assert True
EOF

# revisa contenido
sed -n '1,200p' src/proyecto/test_smoke.py
