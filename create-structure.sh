#!/bin/bash
# Script pour créer la structure complète

# Dossiers
mkdir -p backend/{models,routes,services,utils}
mkdir -p android-app/app/src/main/java/com/padreola/bleauditor
mkdir -p frontend/src/{components,pages,styles}
mkdir -p docs/guides
mkdir -p scripts
mkdir -p tests/{unit,integration}
mkdir -p data/{samples,rules}

# Fichiers
touch backend/app.py backend/requirements.txt backend/config.py
touch backend/models/__init__.py
touch backend/routes/__init__.py
touch backend/services/__init__.py
touch backend/utils/__init__.py

touch android-app/build.gradle
touch android-app/app/src/main/AndroidManifest.xml
touch android-app/app/src/main/java/com/padreola/bleauditor/MainActivity.kt

touch frontend/package.json src/App.jsx src/main.jsx

touch .gitignore LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md CHANGELOG.md
touch setup.py Makefile

touch docs/INSTALL.md docs/ARCHITECTURE.md docs/API.md docs/FAQ.md
touch scripts/install.sh scripts/setup-dev.sh

echo "✅ Structure créée!"
