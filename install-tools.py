import os
import subprocess
import platform

# Detect OS & package manager
def detect_package_manager():
    """Detects the package manager based on the OS."""
    os_type = platform.system()

    if os_type == "Darwin":  # macOS
        return "brew"
    elif os.path.exists("/usr/bin/apt"):
        return "apt"
    elif os.path.exists("/usr/bin/yum"):
        return "yum"
    elif os.path.exists("/usr/bin/dnf"):
        return "dnf"
    elif os.path.exists("/usr/bin/pacman"):
        return "pacman"
    elif os.path.exists("/sbin/apk"):
        return "apk"
    else:
        return None

PACKAGE_MANAGER = detect_package_manager()

# Define install/uninstall commands for each package manager
TOOLS = {
    "Docker": {
        "install": {
            "brew": "brew install --cask docker",
            "apt": "sudo apt update && sudo apt install -y docker.io",
            "yum": "sudo yum install -y docker",
            "dnf": "sudo dnf install -y docker",
            "pacman": "sudo pacman -S docker --noconfirm",
            "apk": "sudo apk add docker"
        },
        "uninstall": {
            "brew": "brew uninstall --cask docker",
            "apt": "sudo apt remove -y docker.io && sudo apt autoremove -y",
            "yum": "sudo yum remove -y docker",
            "dnf": "sudo dnf remove -y docker",
            "pacman": "sudo pacman -Rns docker --noconfirm",
            "apk": "sudo apk del docker"
        }
    },
    "Kubernetes (kubectl)": {
        "install": {
            "brew": "brew install kubectl",
            "apt": "sudo apt update && sudo apt install -y kubectl",
            "yum": "sudo yum install -y kubectl",
            "dnf": "sudo dnf install -y kubectl",
            "pacman": "sudo pacman -S kubectl --noconfirm",
            "apk": "sudo apk add kubectl"
        },
        "uninstall": {
            "brew": "brew uninstall kubectl",
            "apt": "sudo apt remove -y kubectl",
            "yum": "sudo yum remove -y kubectl",
            "dnf": "sudo dnf remove -y kubectl",
            "pacman": "sudo pacman -Rns kubectl --noconfirm",
            "apk": "sudo apk del kubectl"
        }
    },
    "AWS CLI": {
        "install": {
            "brew": "brew install awscli",
            "apt": "curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\" && unzip awscliv2.zip && sudo ./aws/install",
            "yum": "sudo yum install -y aws-cli",
            "dnf": "sudo dnf install -y aws-cli",
            "pacman": "sudo pacman -S aws-cli --noconfirm",
            "apk": "sudo apk add aws-cli"
        },
        "uninstall": {
            "brew": "brew uninstall awscli",
            "apt": "sudo apt remove -y awscli && sudo apt autoremove -y",
            "yum": "sudo yum remove -y aws-cli",
            "dnf": "sudo dnf remove -y aws-cli",
            "pacman": "sudo pacman -Rns aws-cli --noconfirm",
            "apk": "sudo apk del aws-cli"
        }
    },
    "Terraform": {
        "install": {
            "brew": "brew install terraform",
            "apt": "sudo apt update && sudo apt install -y terraform",
            "yum": "sudo yum install -y terraform",
            "dnf": "sudo dnf install -y terraform",
            "pacman": "sudo pacman -S terraform --noconfirm",
            "apk": "sudo apk add terraform"
        },
        "uninstall": {
            "brew": "brew uninstall terraform",
            "apt": "sudo apt remove -y terraform && sudo apt autoremove -y",
            "yum": "sudo yum remove -y terraform",
            "dnf": "sudo dnf remove -y terraform",
            "pacman": "sudo pacman -Rns terraform --noconfirm",
            "apk": "sudo apk del terraform"
        }
    },
    "Helm": {
        "install": {
            "brew": "brew install helm",
            "apt": "sudo apt update && sudo apt install -y helm",
            "yum": "sudo yum install -y helm",
            "dnf": "sudo dnf install -y helm",
            "pacman": "sudo pacman -S helm --noconfirm",
            "apk": "sudo apk add helm"
        },
        "uninstall": {
            "brew": "brew uninstall helm",
            "apt": "sudo apt remove -y helm && sudo apt autoremove -y",
            "yum": "sudo yum remove -y helm",
            "dnf": "sudo dnf remove -y helm",
            "pacman": "sudo pacman -Rns helm --noconfirm",
            "apk": "sudo apk del helm"
        }
    }
}

def execute_command(tool_name, command, action):
    """Runs the command for installation or uninstallation."""
    print(f"\n🔹 {action.capitalize()}ing {tool_name}...\n")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    if result.returncode == 0:
        print(f"✅ {tool_name} {action}ed successfully!")
    else:
        print(f"❌ Failed to {action} {tool_name}. Error:\n{result.stderr}")

def main():
    """User interface to select tools for install/uninstall."""
    if PACKAGE_MANAGER is None:
        print("❌ No supported package manager found! Install Homebrew (Mac) or a Linux package manager.")
        return

    while True:
        print("\n=== DevOps Tool Manager ===")
        print("1. Install a tool")
        print("2. Uninstall a tool")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1" or choice == "2":
            action = "install" if choice == "1" else "uninstall"
            tool_list = list(TOOLS.keys())

            print("\nSelect a tool:")
            for i, tool in enumerate(tool_list, start=1):
                print(f"{i}. {tool}")
            print("0. All Tools")

            tool_choice = input("\nEnter the number: ")

            if tool_choice.isdigit():
                tool_choice = int(tool_choice)
                if tool_choice == 0:
                    for tool, cmds in TOOLS.items():
                        execute_command(tool, cmds[action][PACKAGE_MANAGER], action)
                elif 1 <= tool_choice <= len(tool_list):
                    tool_name = tool_list[tool_choice - 1]
                    execute_command(tool_name, TOOLS[tool_name][action][PACKAGE_MANAGER], action)
                else:
                    print("❌ Invalid selection!")
            else:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            print("🚀 Exiting... Have a great day!")
            break
        else:
            print("❌ Invalid input! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()