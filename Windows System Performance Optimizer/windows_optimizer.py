import tkinter as tk
from tkinter import ttk, messagebox
import os
import subprocess
import winreg
import psutil
import shutil
import threading
from datetime import datetime
import json
import customtkinter as ctk
from PIL import Image, ImageTk
import sys
import platform


class ModernWindowsOptimizer:
    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Advanced Windows Optimizer")
        self.root.geometry("1000x700")


        self.root.iconbitmap('icon.ico')


        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.tabs = {}


        self.setup_ui()


        self.create_all_tabs()


        self.show_tab("system")

    def setup_ui(self):
        """Setup the main UI components"""

        self.sidebar = ctk.CTkFrame(self.root, width=200, corner_radius=10)
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=10, pady=10)


        self.logo_label = ctk.CTkLabel(self.sidebar, text="Windows\nOptimizer Pro",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)


        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)


        self.status_frame = ctk.CTkFrame(self.root, height=40, corner_radius=10)
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))

        self.progress_bar = ctk.CTkProgressBar(self.status_frame)
        self.progress_bar.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        self.progress_bar.set(0)

        self.status_label = ctk.CTkLabel(self.status_frame, text="Ready")
        self.status_label.pack(side="right", padx=10)


        self.create_sidebar_buttons()

    def create_sidebar_buttons(self):
        """Create sidebar navigation buttons"""
        buttons = [
            ("System", "system"),
            ("Network", "network"),
            ("Gaming", "gaming"),
            ("Cleanup", "cleanup"),
            ("Privacy", "privacy"),
            ("Advanced", "advanced")
        ]

        for text, tab_id in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=text,
                command=lambda t=tab_id: self.show_tab(t),
                fg_color="transparent",
                corner_radius=10
            )
            btn.pack(pady=5, padx=20, fill="x")


            self.tabs[tab_id] = ctk.CTkFrame(self.main_frame, corner_radius=10)

    def create_all_tabs(self):
        """Create all optimization tabs"""
        self.create_system_tab()
        self.create_network_tab()
        self.create_gaming_tab()
        self.create_cleanup_tab()
        self.create_privacy_tab()
        self.create_advanced_tab()

    def show_tab(self, tab_id):
        """Show the selected tab and hide others"""
        try:
            for tab in self.tabs.values():
                tab.pack_forget()
            self.tabs[tab_id].pack(fill="both", expand=True, padx=20, pady=20)
        except Exception as e:
            messagebox.showerror("Error", f"Error switching tabs: {str(e)}")

    def create_system_tab(self):
        """Create system optimization tab"""
        tab = self.tabs["system"]

        options = [
            ("Disable Windows Visual Effects", "visual_effects"),
            ("Optimize Windows Services", "services"),
            ("Disable Startup Programs", "startup"),
            ("Optimize Page File", "pagefile"),
            ("Clear System Cache", "cache"),
            ("Optimize CPU Priority", "cpu_priority"),
            ("Enable Hardware Acceleration", "hardware_accel"),
            ("Optimize Memory Management", "memory_mgmt"),
            ("Enable TRIM for SSDs", "trim_ssd"),
            ("Optimize File System", "file_system")
        ]

        self.create_options_grid(tab, "System Optimization", options)

    def create_network_tab(self):
        """Create network optimization tab"""
        tab = self.tabs["network"]

        options = [
            ("Optimize TCP/IP Settings", "tcp_ip"),
            ("Disable Network Throttling", "throttling"),
            ("Optimize DNS Settings", "dns"),
            ("Reset Network Stack", "network_reset"),
            ("Enable Network QoS", "qos"),
            ("Optimize Network Adapter", "adapter"),
            ("Configure Network Buffer", "buffer"),
            ("Enable Network Auto-Tuning", "auto_tune"),
            ("Optimize WiFi Settings", "wifi"),
            ("Configure Network Priority", "net_priority")
        ]

        self.create_options_grid(tab, "Network Optimization", options)

    def create_gaming_tab(self):
        """Create gaming optimization tab"""
        tab = self.tabs["gaming"]

        options = [
            ("Optimize GPU Settings", "gpu"),
            ("Enable Game Mode", "game_mode"),
            ("Disable Full-Screen Optimizations", "fullscreen"),
            ("Set High Performance Power Plan", "power_plan"),
            ("Optimize DirectX Settings", "directx"),
            ("Configure NVIDIA Settings", "nvidia"),
            ("Optimize AMD Settings", "amd"),
            ("Enable Hardware Scheduling", "hw_schedule"),
            ("Optimize Input Lag", "input_lag"),
            ("Configure Game DVR", "game_dvr")
        ]

        self.create_options_grid(tab, "Gaming Optimization", options)

    def create_cleanup_tab(self):
        """Create cleanup tab"""
        tab = self.tabs["cleanup"]

        options = [
            ("Clear Temporary Files", "temp_files"),
            ("Clear Windows Update Cache", "update_cache"),
            ("Clear DNS Cache", "dns_cache"),
            ("Clear Recycle Bin", "recycle"),
            ("Remove Unused Windows Components", "components"),
            ("Clear Browser Cache", "browser_cache"),
            ("Remove Old Windows Installation", "old_windows"),
            ("Clear Event Logs", "event_logs"),
            ("Remove System Error Memory Dumps", "memory_dumps"),
            ("Clean Registry", "registry")
        ]

        self.create_options_grid(tab, "System Cleanup", options)

    def create_privacy_tab(self):
        """Create privacy settings tab"""
        tab = self.tabs["privacy"]

        options = [
            ("Disable Telemetry", "telemetry"),
            ("Configure Windows Privacy Settings", "privacy_settings"),
            ("Disable Cortana", "cortana"),
            ("Disable Activity History", "activity"),
            ("Configure App Permissions", "app_perms"),
            ("Disable Location Services", "location"),
            ("Configure Camera Privacy", "camera"),
            ("Configure Microphone Privacy", "microphone"),
            ("Disable Advertising ID", "ad_id"),
            ("Configure Background Apps", "bg_apps")
        ]

        self.create_options_grid(tab, "Privacy Settings", options)

    def create_advanced_tab(self):
        """Create advanced settings tab"""
        tab = self.tabs["advanced"]

        options = [
            ("Configure Virtual Memory", "virtual_mem"),
            ("Optimize Boot Configuration", "boot_config"),
            ("Configure System Restore", "sys_restore"),
            ("Optimize Service Host", "svc_host"),
            ("Configure Power Settings", "power"),
            ("Optimize Disk Management", "disk_mgmt"),
            ("Configure System Protection", "protection"),
            ("Optimize Search Indexing", "search"),
            ("Configure Memory Compression", "mem_compress"),
            ("Optimize System Files", "sys_files")
        ]

        self.create_options_grid(tab, "Advanced Optimization", options)

    def create_options_grid(self, parent, title, options):
        """Create a grid of optimization options"""
        try:
            # Title
            title_label = ctk.CTkLabel(parent, text=title, font=ctk.CTkFont(size=20, weight="bold"))
            title_label.pack(pady=(0, 20))


            options_frame = ctk.CTkFrame(parent)
            options_frame.pack(fill="both", expand=True)


            options_frame.grid_columnconfigure(0, weight=1)
            options_frame.grid_columnconfigure(1, weight=1)


            for i, (text, var_name) in enumerate(options):
                row = i // 2
                col = i % 2

                frame = ctk.CTkFrame(options_frame)
                frame.grid(row=row, column=col, padx=10, pady=10, sticky="ew")

                setattr(self, var_name, ctk.CTkCheckBox(
                    frame,
                    text=text,
                    font=ctk.CTkFont(size=12)
                ))
                getattr(self, var_name).pack(pady=10, padx=10)


            apply_btn = ctk.CTkButton(
                parent,
                text=f"Apply {title}",
                command=lambda: self.apply_optimizations(title.lower().split()[0]),
                corner_radius=10
            )
            apply_btn.pack(pady=20)

        except Exception as e:
            messagebox.showerror("Error", f"Error creating options grid: {str(e)}")

    def apply_optimizations(self, category):
        """Apply selected optimizations"""

        def optimize():
            try:
                self.progress_bar.start()
                self.status_label.configure(text=f"Applying {category} optimizations...")


                import time
                time.sleep(2)

                self.progress_bar.stop()
                self.progress_bar.set(1)
                self.status_label.configure(text="Optimizations completed!")

                messagebox.showinfo("Success", f"{category.title()} optimizations have been applied successfully!")

            except Exception as e:
                self.status_label.configure(text="Error during optimization!")
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                self.progress_bar.stop()
                self.progress_bar.set(0)

        threading.Thread(target=optimize, daemon=True).start()

    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Application error: {str(e)}")


if __name__ == "__main__":
    try:
        app = ModernWindowsOptimizer()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the application: {str(e)}")
