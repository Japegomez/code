import { CommonModule } from '@angular/common';
import { Component, Input, output } from '@angular/core';
import { MatButtonToggleModule } from "@angular/material/button-toggle";

@Component({
  selector: 'app-toggle-button',
  standalone: true,
  imports: [MatButtonToggleModule, CommonModule ],
  templateUrl: './toggle-button.component.html',
  styleUrl: './toggle-button.component.css'
})
export class ToggleButtonComponent {
  @Input() buttonSelected!: string;
  buttonSelectedChange = output<string>()
  
  // ngOnInit() {
  //   this.valueChange.emit(this.buttonSelected);
  // }

  changeButtonSelected(value: string) {
    this.buttonSelected = value;
    this.buttonSelectedChange.emit(value);
  }
}
