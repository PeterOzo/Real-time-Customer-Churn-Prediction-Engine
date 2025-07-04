# -*- coding: utf-8 -*-
"""create_config.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uAWzJn879Ty4j0Tytw2iDs7u2zteJeQI
"""

#!/usr/bin/env python3
"""
Automatic .streamlit/config.toml Creator
Run this script in your project folder to automatically create the configuration file
"""

import os

def create_streamlit_config():
    """
    Creates .streamlit/config.toml file with optimal settings for ACA Dashboard
    """

    # Create .streamlit directory if it doesn't exist
    config_dir = ".streamlit"
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
        print(f"✅ Created directory: {config_dir}")
    else:
        print(f"📁 Directory already exists: {config_dir}")

    # Configuration content optimized for ACA Pricing Dashboard
    config_content = """[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
maxMessageSize = 200
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
showErrorDetails = false

[logger]
level = "info"

[client]
caching = true
displayEnabled = true
"""

    # Write config file
    config_path = os.path.join(config_dir, "config.toml")
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(config_content)
        print(f"✅ Created config file: {config_path}")
        print("🎯 Configuration optimized for ACA Pricing Dashboard!")

        # Verify the file was created
        if os.path.exists(config_path):
            file_size = os.path.getsize(config_path)
            print(f"📄 File size: {file_size} bytes")
            print("🚀 Ready for Streamlit Cloud deployment!")

    except Exception as e:
        print(f"❌ Error creating config file: {e}")
        return False

    return True

def show_project_structure():
    """
    Shows the current project structure
    """
    print("\n📁 Current Project Structure:")
    print("=" * 40)

    for root, dirs, files in os.walk("."):
        level = root.replace(".", "").count(os.sep)
        indent = " " * 2 * level
        print(f"{indent}{os.path.basename(root)}/")

        subindent = " " * 2 * (level + 1)
        for file in files:
            if not file.startswith('.'):  # Hide hidden files except our config
                print(f"{subindent}{file}")
            elif file == "config.toml":
                print(f"{subindent}✅ {file}")

def main():
    """
    Main function to create Streamlit configuration
    """
    print("🎯 ACA Pricing Dashboard - Config Creator")
    print("=" * 50)
    print("This script will create .streamlit/config.toml for optimal performance\n")

    # Check if we're in the right directory
    if os.path.exists("app.py") or any(f.endswith('.py') for f in os.listdir('.')):
        print("📍 Detected Python project - proceeding with config creation\n")
    else:
        print("⚠️  No Python files detected. Make sure you're in your project directory.\n")

    # Create the configuration
    success = create_streamlit_config()

    if success:
        print("\n" + "=" * 50)
        print("🎉 SUCCESS! Your Streamlit configuration is ready!")
        print("=" * 50)

        # Show what was created
        show_project_structure()

        print("\n🚀 Next Steps:")
        print("1. Test locally: streamlit run app.py")
        print("2. Commit to GitHub: git add . && git commit -m 'Add Streamlit config'")
        print("3. Deploy to Streamlit Cloud")
        print("\n💡 Your dashboard will now have:")
        print("   - Optimized blue theme matching your design")
        print("   - Enhanced performance settings")
        print("   - Professional appearance")
        print("   - Security configurations")

    else:
        print("\n❌ Configuration creation failed. Please check permissions and try again.")

if __name__ == "__main__":
    main()
