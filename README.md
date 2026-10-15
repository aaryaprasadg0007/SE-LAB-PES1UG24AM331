# Lab 3 - Component Modelling & Architectural Pattern Selection

**Scenario:** Self-Service Coffee Kiosk System  
**Architecture selected:** Layered architecture  
**Student:** Aarya Prasad G  
**SRN:** PES1UG24AM331

## Submission files

- `Lab3_Component_Diagram.pdf` - component diagram in PDF format (required deliverable).
- `Lab3_Component_Diagram.png` - PNG preview of the diagram.
- `Lab3_Component_Diagram.svg` - editable vector source for the diagram.
- `Lab3_Architecture_Justification.pdf` - one-page written justification (required deliverable).
- `Lab3_Architecture_Justification.docx` - editable Word copy of the justification.
- `README.md` - this overview and short architecture comparison.

## Component and interface summary

The diagram contains five components: Touchscreen UI, Order Manager, Payment Service, Receipt Printer Adapter, and Menu & Pricing Database. Four named interfaces are shown using UML provided-interface balls and required-interface sockets:

- `OrderControl` - order submission and checkout status between the UI and Order Manager.
- `CardPayment` - payment authorization and result between Order Manager and Payment Service.
- `ReceiptPrint` - receipt data sent from Order Manager to Receipt Printer Adapter.
- `MenuCatalog` - menu and price lookup between Order Manager and Menu & Pricing Database.

The menu supports Espresso, Americano and Latte, with Small and Large sizes. The payment option is credit card only, and the receipt adapter connects the software flow to the printer hardware.

## Brief architectural comparison

- **Layered architecture:** separates presentation, business/hardware integration, and data concerns. It suits this small, fixed kiosk workflow and is easy to understand and test. Calls should remain simple to limit unnecessary overhead.
- **Microservices architecture:** allows independent deployment and scaling, but adds service-operation, network, and data-consistency complexity that is not needed for this kiosk's limited scope.
- **Client-server architecture:** gives centralized control and data consistency, but does not communicate the internal separation of UI, order logic, payment/printer integration, and data as clearly as the selected layered design.

## Final check before submission

Confirm that the `Lab3` folder is in the intended course repository and that the diagram PDF and one-page justification PDF open correctly after upload. The PNG and SVG are included as convenient preview/editing files; the handout requires the diagram in PNG or PDF and the justification as PDF.
