"""
Shopping Cart — tkinter GUI
Run with:  python shopping_cart.py
No third-party libraries required.
"""

import tkinter as tk
from tkinter import messagebox, ttk
from dataclasses import dataclass, field
from typing import List

# ── palette ──────────────────────────────────────────────────────────────────
BG          = "#f7f8fa"
WHITE       = "#ffffff"
SURFACE     = "#ffffff"
BORDER      = "#e2e8f0"
TEXT        = "#1e293b"
TEXT_MUTED  = "#64748b"
ACCENT      = "#2563eb"
ACCENT_HVR  = "#1d4ed8"
DANGER      = "#ef4444"
DANGER_HVR  = "#dc2626"
SUCCESS     = "#16a34a"
HEADER_BG   = "#1e293b"
HEADER_FG   = "#f8fafc"
ROW_ALT     = "#f1f5f9"
TOTAL_BG    = "#eff6ff"
TOTAL_FG    = "#1d4ed8"


# ── data model ────────────────────────────────────────────────────────────────
@dataclass
class CartItem:
    name: str
    price: float
    qty: int = 1

    @property
    def subtotal(self) -> float:
        return round(self.price * self.qty, 2)


@dataclass
class Cart:
    items: List[CartItem] = field(default_factory=list)

    def add(self, name: str, price: float) -> None:
        """Add item or increment qty if item already exists."""
        name = name.strip().title()
        for item in self.items:
            if item.name.lower() == name.lower():
                item.qty += 1
                return
        self.items.append(CartItem(name, price))

    def remove(self, index: int) -> None:
        if 0 <= index < len(self.items):
            self.items.pop(index)

    def update_qty(self, index: int, qty: int) -> None:
        if 0 <= index < len(self.items):
            if qty <= 0:
                self.remove(index)
            else:
                self.items[index].qty = qty

    def clear(self) -> None:
        self.items.clear()

    @property
    def total(self) -> float:
        return round(sum(i.subtotal for i in self.items), 2)

    @property
    def item_count(self) -> int:
        return sum(i.qty for i in self.items)


# ── reusable widget helpers ───────────────────────────────────────────────────
def styled_button(parent, text, command, color=ACCENT, hover=ACCENT_HVR,
                  fg="white", width=None, font_size=11):
    btn = tk.Button(
        parent, text=text, command=command,
        bg=color, fg=fg, activebackground=hover, activeforeground=fg,
        font=("Helvetica", font_size, "bold"), relief="flat", bd=0,
        cursor="hand2", padx=14, pady=7,
        **({"width": width} if width else {})
    )
    btn.bind("<Enter>", lambda e: btn.configure(bg=hover))
    btn.bind("<Leave>", lambda e: btn.configure(bg=color))
    return btn


def label(parent, text, size=12, weight="normal", color=TEXT, bg=None):
    return tk.Label(
        parent, text=text,
        font=("Helvetica", size, weight),
        fg=color, bg=bg or parent["bg"]
    )


# ── main application ──────────────────────────────────────────────────────────
class ShoppingCartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping Cart")
        self.configure(bg=BG)
        self.resizable(True, True)
        self.minsize(560, 540)
        self.geometry("640x620")

        self.cart = Cart()
        self._build_ui()
        self._refresh()

    # ── layout construction ───────────────────────────────────────────────────

    def _build_ui(self):
        # ── header ────────────────────────────────────────────────────────────
        hdr = tk.Frame(self, bg=HEADER_BG)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🛒  Shopping Cart",
                 font=("Helvetica", 17, "bold"),
                 bg=HEADER_BG, fg=HEADER_FG).pack(side="left", padx=20, pady=14)
        self.item_count_badge = tk.Label(
            hdr, text="", font=("Helvetica", 10, "bold"),
            bg="#3b82f6", fg="white", padx=8, pady=3)
        self.item_count_badge.pack(side="left", pady=14)

        # ── add-item panel ────────────────────────────────────────────────────
        add_card = tk.Frame(self, bg=WHITE, bd=0, highlightthickness=1,
                            highlightbackground=BORDER)
        add_card.pack(fill="x", padx=16, pady=(14, 0))

        label(add_card, "Add item", size=12, weight="bold", bg=WHITE).pack(
            anchor="w", padx=14, pady=(12, 8))

        fields = tk.Frame(add_card, bg=WHITE)
        fields.pack(fill="x", padx=14, pady=(0, 12))
        fields.columnconfigure(0, weight=3)
        fields.columnconfigure(1, weight=1)
        fields.columnconfigure(2, weight=0)

        # item name
        tk.Label(fields, text="Item name", font=("Helvetica", 10),
                 bg=WHITE, fg=TEXT_MUTED).grid(row=0, column=0, sticky="w", pady=(0, 3))
        tk.Label(fields, text="Price (₹)", font=("Helvetica", 10),
                 bg=WHITE, fg=TEXT_MUTED).grid(row=0, column=1, sticky="w", padx=(10, 0), pady=(0, 3))

        self.name_var  = tk.StringVar()
        self.price_var = tk.StringVar()

        name_entry = tk.Entry(fields, textvariable=self.name_var,
                              font=("Helvetica", 12), bd=0, relief="flat",
                              bg=BG, fg=TEXT, insertbackground=TEXT)
        name_entry.grid(row=1, column=0, sticky="ew", ipady=7, padx=(0, 0))
        name_entry.bind("<Return>", lambda e: self.price_entry.focus())

        self.price_entry = tk.Entry(fields, textvariable=self.price_var,
                                    font=("Helvetica", 12), bd=0, relief="flat",
                                    bg=BG, fg=TEXT, insertbackground=TEXT, width=10)
        self.price_entry.grid(row=1, column=1, sticky="ew", ipady=7, padx=(10, 10))
        self.price_entry.bind("<Return>", lambda e: self._add_item())

        add_btn = styled_button(fields, "Add  +", self._add_item, font_size=12)
        add_btn.grid(row=1, column=2)

        self.error_label = tk.Label(add_card, text="", font=("Helvetica", 10),
                                    fg=DANGER, bg=WHITE)
        self.error_label.pack(anchor="w", padx=14, pady=(0, 4))

        # ── cart table ────────────────────────────────────────────────────────
        table_header = tk.Frame(self, bg=HEADER_BG)
        table_header.pack(fill="x", padx=16, pady=(14, 0))
        for col, w, anchor in [("Item", 260, "w"), ("Price", 90, "center"),
                                ("Qty", 60, "center"), ("Subtotal", 90, "e"),
                                ("", 60, "center")]:
            tk.Label(table_header, text=col,
                     font=("Helvetica", 10, "bold"),
                     bg=HEADER_BG, fg="#94a3b8",
                     width=w // 8, anchor=anchor).pack(side="left", padx=6, pady=7)

        # scrollable canvas for rows
        self.canvas_frame = tk.Frame(self, bg=BG)
        self.canvas_frame.pack(fill="both", expand=True, padx=16)

        self.canvas = tk.Canvas(self.canvas_frame, bg=BG, bd=0,
                                highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.canvas_frame, orient="vertical",
                                  command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.rows_frame = tk.Frame(self.canvas, bg=BG)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.rows_frame, anchor="nw")

        self.rows_frame.bind("<Configure>", self._on_rows_configure)
        self.canvas.bind("<Configure>", self._on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>",
                             lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        # ── footer: total + actions ───────────────────────────────────────────
        footer = tk.Frame(self, bg=WHITE, bd=0, highlightthickness=1,
                          highlightbackground=BORDER)
        footer.pack(fill="x", padx=16, pady=(0, 16))

        total_row = tk.Frame(footer, bg=TOTAL_BG)
        total_row.pack(fill="x")
        label(total_row, "Total", size=13, weight="bold",
              color=TOTAL_FG, bg=TOTAL_BG).pack(side="left", padx=16, pady=12)
        self.total_label = tk.Label(total_row, text="₹0.00",
                                    font=("Helvetica", 18, "bold"),
                                    fg=TOTAL_FG, bg=TOTAL_BG)
        self.total_label.pack(side="right", padx=16, pady=12)

        action_row = tk.Frame(footer, bg=WHITE)
        action_row.pack(fill="x", padx=14, pady=10)
        styled_button(action_row, "Clear cart", self._clear_cart,
                      color=DANGER, hover=DANGER_HVR).pack(side="left")
        styled_button(action_row, "Checkout  →", self._checkout,
                      color=SUCCESS, hover="#15803d",
                      font_size=12).pack(side="right")

    # ── canvas resize helpers ─────────────────────────────────────────────────

    def _on_rows_configure(self, _event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)

    # ── cart actions ──────────────────────────────────────────────────────────

    def _add_item(self):
        name  = self.name_var.get().strip()
        price = self.price_var.get().strip()

        if not name:
            self._show_error("Item name cannot be empty.")
            return
        if not price:
            self._show_error("Price cannot be empty.")
            return
        try:
            price_val = float(price)
            if price_val < 0:
                raise ValueError
        except ValueError:
            self._show_error("Enter a valid positive price.")
            return

        self.cart.add(name, price_val)
        self.name_var.set("")
        self.price_var.set("")
        self.error_label.configure(text="")
        self._refresh()

    def _remove_item(self, index: int):
        self.cart.remove(index)
        self._refresh()

    def _change_qty(self, index: int, delta: int):
        new_qty = self.cart.items[index].qty + delta
        self.cart.update_qty(index, new_qty)
        self._refresh()

    def _clear_cart(self):
        if not self.cart.items:
            return
        if messagebox.askyesno("Clear cart", "Remove all items from your cart?"):
            self.cart.clear()
            self._refresh()

    def _checkout(self):
        if not self.cart.items:
            messagebox.showinfo("Cart is empty", "Add some items before checking out.")
            return

        lines = "\n".join(
            f"  {i.name:<22} ×{i.qty}   ₹{i.subtotal:.2f}"
            for i in self.cart.items
        )
        summary = (
            f"{'─'*44}\n"
            f"{lines}\n"
            f"{'─'*44}\n"
            f"  {'Total':<28}  ₹{self.cart.total:.2f}\n"
            f"{'─'*44}"
        )
        if messagebox.askyesno("Confirm order",
                               f"Place order?\n\n{summary}",
                               icon="question"):
            self.cart.clear()
            self._refresh()
            messagebox.showinfo("Order placed",
                                "Your order has been placed. Thank you! 🎉")

    # ── show error ────────────────────────────────────────────────────────────

    def _show_error(self, msg: str):
        self.error_label.configure(text=msg)
        self.after(3000, lambda: self.error_label.configure(text=""))

    # ── refresh UI ────────────────────────────────────────────────────────────

    def _refresh(self):
        # clear rows
        for w in self.rows_frame.winfo_children():
            w.destroy()

        if not self.cart.items:
            empty = tk.Frame(self.rows_frame, bg=BG)
            empty.pack(fill="x", pady=40)
            tk.Label(empty, text="Your cart is empty",
                     font=("Helvetica", 13), fg=TEXT_MUTED, bg=BG).pack()
            tk.Label(empty, text="Add an item above to get started.",
                     font=("Helvetica", 11), fg=TEXT_MUTED, bg=BG).pack(pady=4)
        else:
            for idx, item in enumerate(self.cart.items):
                row_bg = WHITE if idx % 2 == 0 else ROW_ALT
                row = tk.Frame(self.rows_frame, bg=row_bg,
                               bd=0, highlightthickness=1,
                               highlightbackground=BORDER)
                row.pack(fill="x", pady=(0, 1))

                # name
                tk.Label(row, text=item.name,
                         font=("Helvetica", 12), fg=TEXT,
                         bg=row_bg, anchor="w", width=22).pack(
                    side="left", padx=(12, 0), pady=10)

                # unit price
                tk.Label(row, text=f"₹{item.price:.2f}",
                         font=("Helvetica", 11), fg=TEXT_MUTED,
                         bg=row_bg, width=9, anchor="center").pack(side="left")

                # qty controls
                qty_frame = tk.Frame(row, bg=row_bg)
                qty_frame.pack(side="left", padx=4)
                tk.Button(qty_frame, text="−", font=("Helvetica", 12, "bold"),
                          bg=row_bg, fg=TEXT_MUTED, activebackground=BORDER,
                          relief="flat", bd=0, cursor="hand2", padx=6,
                          command=lambda i=idx: self._change_qty(i, -1)
                          ).pack(side="left")
                tk.Label(qty_frame, text=str(item.qty),
                         font=("Helvetica", 12, "bold"), fg=TEXT,
                         bg=row_bg, width=3, anchor="center").pack(side="left")
                tk.Button(qty_frame, text="+", font=("Helvetica", 12, "bold"),
                          bg=row_bg, fg=TEXT_MUTED, activebackground=BORDER,
                          relief="flat", bd=0, cursor="hand2", padx=6,
                          command=lambda i=idx: self._change_qty(i, 1)
                          ).pack(side="left")

                # subtotal
                tk.Label(row, text=f"₹{item.subtotal:.2f}",
                         font=("Helvetica", 12, "bold"), fg=TEXT,
                         bg=row_bg, width=9, anchor="e").pack(side="left")

                # remove
                tk.Button(row, text="✕", font=("Helvetica", 11),
                          bg=row_bg, fg=DANGER, activebackground=BORDER,
                          relief="flat", bd=0, cursor="hand2", padx=10,
                          command=lambda i=idx: self._remove_item(i)
                          ).pack(side="right", padx=6)

        # update totals & badge
        self.total_label.configure(text=f"₹{self.cart.total:.2f}")
        count = self.cart.item_count
        if count:
            self.item_count_badge.configure(
                text=f" {count} item{'s' if count != 1 else ''} ")
            self.item_count_badge.pack(side="left", pady=14)
        else:
            self.item_count_badge.pack_forget()

        self.canvas.update_idletasks()
        self._on_rows_configure()


# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = ShoppingCartApp()
    app.mainloop()
