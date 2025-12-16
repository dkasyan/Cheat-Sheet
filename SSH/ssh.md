# SSH - Zarządzanie kluczami SSH

## Spis treści
- [Generowanie klucza SSH](#generowanie-klucza-ssh)
- [Dodawanie klucza do ssh-agent](#dodawanie-klucza-do-ssh-agent)
- [Kopiowanie klucza publicznego na serwer](#kopiowanie-klucza-publicznego-na-serwer)
- [Zarządzanie kluczami](#zarządzanie-kluczami)
- [Konfiguracja SSH](#konfiguracja-ssh)

## Generowanie klucza SSH

### Podstawowa komenda
```bash
ssh-keygen -t ed25519 -C "twoj.email@example.com"
```

### Opcje algorytmów szyfrowania
```bash
# ED25519 (zalecany - nowoczesny, bezpieczny, szybki)
ssh-keygen -t ed25519 -C "twoj.email@example.com"

# RSA 4096-bit (starszy standard, nadal bezpieczny)
ssh-keygen -t rsa -b 4096 -C "twoj.email@example.com"
```

### Proces generowania
1. Uruchom komendę generującą klucz
2. Podaj ścieżkę do pliku (domyślnie: `~/.ssh/id_ed25519`) lub wciśnij Enter
3. Wprowadź hasło (passphrase) dla dodatkowego zabezpieczenia lub zostaw puste
4. Potwierdź hasło

### Lokalizacja kluczy
Po wygenerowaniu otrzymasz dwa pliki:
- `~/.ssh/id_ed25519` - klucz prywatny (NIGDY nie udostępniaj!)
- `~/.ssh/id_ed25519.pub` - klucz publiczny (ten możesz udostępniać)

## Dodawanie klucza do ssh-agent

### Uruchomienie ssh-agent
```bash
# Uruchom agenta w tle
eval "$(ssh-agent -s)"
```

### Dodanie klucza prywatnego
```bash
# Dodaj klucz ED25519
ssh-add ~/.ssh/id_ed25519

# Dodaj klucz RSA
ssh-add ~/.ssh/id_rsa
```

### macOS - trwałe dodanie klucza
Edytuj lub utwórz plik `~/.ssh/config`:
```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

### Sprawdzenie załadowanych kluczy
```bash
ssh-add -l
```

## Kopiowanie klucza publicznego na serwer

### Metoda 1: ssh-copy-id (zalecana)
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@hostname
```

### Metoda 2: Ręczne kopiowanie
```bash
# Wyświetl klucz publiczny
cat ~/.ssh/id_ed25519.pub

# Połącz się z serwerem i dodaj klucz
ssh user@hostname
mkdir -p ~/.ssh
echo "TWOJ_KLUCZ_PUBLICZNY" >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### Metoda 3: Jednolinijkowa komenda
```bash
cat ~/.ssh/id_ed25519.pub | ssh user@hostname "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

## Zarządzanie kluczami

### Wyświetlenie klucza publicznego
```bash
cat ~/.ssh/id_ed25519.pub
```

### Zmiana hasła klucza
```bash
ssh-keygen -p -f ~/.ssh/id_ed25519
```

### Usunięcie klucza z ssh-agent
```bash
# Usuń konkretny klucz
ssh-add -d ~/.ssh/id_ed25519

# Usuń wszystkie klucze
ssh-add -D
```

### Lista kluczy w ssh-agent
```bash
# Krótka lista
ssh-add -l

# Szczegółowa lista z kluczami publicznymi
ssh-add -L
```

## Konfiguracja SSH

### Plik konfiguracyjny ~/.ssh/config

```
# Konfiguracja dla GitHub
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github
  IdentitiesOnly yes

# Konfiguracja dla serwera produkcyjnego
Host prod-server
  HostName 192.168.1.100
  User admin
  Port 2222
  IdentityFile ~/.ssh/id_ed25519
  ServerAliveInterval 60

# Konfiguracja dla wszystkich hostów w domenie
Host *.example.com
  User developer
  IdentityFile ~/.ssh/id_ed25519_work
  ForwardAgent yes
```

### Testowanie połączenia
```bash
# Test połączenia z serwerem
ssh -T user@hostname

# Test z GitHub
ssh -T git@github.com

# Test z verbose mode (diagnostyka)
ssh -vT user@hostname
```

### Uprawnienia plików SSH
```bash
# Prawidłowe uprawnienia
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/authorized_keys
```

## Najlepsze praktyki

1. **Używaj ED25519** - szybszy i bezpieczniejszy niż RSA
2. **Zawsze używaj hasła (passphrase)** - dodatkowa warstwa zabezpieczeń
3. **Jeden klucz na serwis** - łatwiejsze zarządzanie i revokacja
4. **Nie udostępniaj klucza prywatnego** - tylko klucz publiczny
5. **Regularnie rotuj klucze** - szczególnie w środowiskach produkcyjnych
6. **Używaj ssh-agent** - nie musisz podawać hasła przy każdym połączeniu
7. **Backup kluczy** - zachowaj kopię w bezpiecznym miejscu

## Rozwiązywanie problemów

### Permission denied (publickey)
```bash
# Sprawdź czy klucz jest załadowany
ssh-add -l

# Spróbuj połączyć się z verbose mode
ssh -v user@hostname

# Sprawdź uprawnienia plików
ls -la ~/.ssh/
```

### Agent nie działa
```bash
# Restart agenta
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### Zbyt otwarte uprawnienia
```bash
# Napraw uprawnienia
chmod 700 ~/.ssh
chmod 600 ~/.ssh/*
chmod 644 ~/.ssh/*.pub
```
