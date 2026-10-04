# Pytest Fundamentals — Tasklar, İzah, Həll

## Struktur
```
app/            # test olunan kod (calculator.py, bank.py, utils.py)
tests/          # həllər (hər task üçün 1 fayl) + conftest.py
pytest.ini      # konfiqurasiya (testpaths, pythonpath, marker-lər)
```

## İşə salmaq
```bash
python3 -m venv .venv && .venv/bin/pip install pytest
.venv/bin/pytest -v                 # hamısı, ətraflı
.venv/bin/pytest tests/test_03_parametrize.py   # bir fayl
.venv/bin/pytest -k "deposit"       # adında "deposit" olan testlər
.venv/bin/pytest -m smoke           # yalnız @pytest.mark.smoke
.venv/bin/pytest -x                 # ilk xətada dayan
```

---

## Task 1 — Sadə `assert`
**Tapşırıq:** `add()` və `is_even()` üçün test yaz.
**İzah:** Pytest test faylını `test_*.py`, funksiyanı `test_*` adından tanıyır. Xüsusi `assertEqual` lazım deyil — adi `assert` kifayətdir, pytest xəta zamanı hər iki tərəfin dəyərini göstərir.
**Həll:** `tests/test_01_assert.py`

## Task 2 — Exception yoxlamaq
**Tapşırıq:** `divide(x, 0)` `ZeroDivisionError` atdığını və mesajını yoxla.
**İzah:** `with pytest.raises(Xəta):` blokunun içində həmin xəta atılmasa test FAIL olur. `match=` mesajı regex ilə yoxlayır.
**Həll:** `tests/test_02_raises.py`

## Task 3 — Parametrize
**Tapşırıq:** `add()`-ı 4 fərqli data dəsti ilə, tək test funksiyası ilə yoxla.
**İzah:** `@pytest.mark.parametrize("a, b, expected", [...])` — hər sətir ayrıca test kimi işləyir (`test_add[1-2-3]`). `ids=` test adlarını oxunaqlı edir. Kod təkrarını aradan qaldırır.
**Həll:** `tests/test_03_parametrize.py`

## Task 4 — Fixture və `conftest.py`
**Tapşırıq:** `BankAccount` üçün hazır obyekt verən fixture yarat, deposit/withdraw test et.
**İzah:** `@pytest.fixture` test üçün hazırlıq (setup) verir. Test funksiyası parametr adı ilə fixture-u alır (dependency injection). Default `scope="function"` — hər test **təzə** obyekt alır, testlər bir-birinə təsir etmir. `conftest.py`-dakı fixture-lar import etmədən bütün testlərdə görünür.
**Həll:** `tests/conftest.py`, `tests/test_04_fixtures.py`

## Task 5 — `yield` fixture və scope
**Tapşırıq:** "DB connection" fixture-u yarat: əvvəl connect, sonda disconnect; modul üçün bir dəfə.
**İzah:** `yield`-dən əvvəlki hissə setup, sonrakı hissə teardown-dur (test fail olsa belə işləyir). `scope`: `function` < `class` < `module` < `package` < `session`. Bahalı resurslar (DB, browser) üçün böyük scope istifadə olunur.
**Həll:** `tests/test_05_yield_scope.py`

## Task 6 — Marker-lər
**Tapşırıq:** Testləri `skip`, `skipif`, `xfail`, və custom (`smoke`, `slow`) ilə işarələ.
**İzah:**
- `skip` — testi heç işlətmə
- `skipif(şərt)` — şərt doğrudursa keç
- `xfail` — "fail olacağını bilirik"; fail olarsa XFAIL, keçərsə XPASS
- custom marker-lər `pytest.ini`-də qeydiyyatdan keçirilir, `-m smoke` ilə seçilir
**Həll:** `tests/test_06_markers.py`

## Task 7 — `pytest.approx`
**Tapşırıq:** `0.1 + 0.2 == 0.3` müqayisəsini düzgün yoxla.
**İzah:** Float-lar binary-də dəqiq saxlanmır (`0.30000000000000004`). `pytest.approx` tolerantlıqla müqayisə edir; `rel=` / `abs=` ilə dəqiqliyi təyin etmək olar.
**Həll:** `tests/test_07_approx.py`

## Task 8 — Daxili fixture-lar
**Tapşırıq:** Fayl yazıb-oxumağı, `print` çıxışını və environment dəyişənini test et.
**İzah:**
- `tmp_path` — hər test üçün müvəqqəti qovluq (`pathlib.Path`)
- `capsys` — `stdout`/`stderr`-i tutur: `capsys.readouterr().out`
- `monkeypatch` — env var, atribut, funksiyanı müvəqqəti dəyişir; test bitəndə avtomatik bərpa edir
**Həll:** `tests/test_08_builtin_fixtures.py`

---

## Əlavə tasklar (həlli: `tests/test_09_extra.py`, `tests/test_10_session.py`)
1. `BankAccount.deposit(-10)` `ValueError` atdığını test et.
2. `divide()` üçün 5 halı parametrize et (mənfi, float, böyük ədədlər).
3. `scope="session"` fixture yaz və bir neçə faylda istifadə et.
4. `monkeypatch.setattr` ilə `app.utils.get_env_mode`-u əvəz edib test yaz.
5. Parametrize + fixture birləşdir: müxtəlif başlanğıc balanslarla hesab yarat.

### Əlavə taskların izahı
1. **Mənfi deposit** — `pytest.raises(ValueError)` + xətadan sonra balansın dəyişmədiyini yoxlayırıq.
2. **divide() 5 hal** — `parametrize` + `ids`; float nəticələr üçün `pytest.approx`.
3. **Session fixture** — `conftest.py`-da `scope="session"`; iki fərqli faylda istifadə olunur, `SESSION_CALLS` sayğacı 1 dəfə yaradıldığını sübut edir.
4. **monkeypatch.setattr** — `monkeypatch.setattr(utils, "get_env_mode", lambda: "mocked")`. Növbəti test orijinalın bərpa olunduğunu yoxlayır.
   ⚠️ Patch-i funksiyanın **istifadə olunduğu** modulda et: `from app.utils import get_env_mode` ilə import edilmiş kopyaya `app.utils` üzərindən etdiyin patch təsir etmir.
5. **Parametrize olunmuş fixture** — `@pytest.fixture(params=[0, 50, 1000])` + `request.param`. Bu fixture-u istifadə edən hər test 3 dəfə işləyir.
