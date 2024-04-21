import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';
import { MatButtonToggleModule } from "@angular/material/button-toggle";

@Component({
  selector: 'app-toggle-button',
  standalone: true,
  imports: [MatButtonToggleModule, CommonModule ],
  templateUrl: './toggle-button.component.html',
  styleUrl: './toggle-button.component.css'
})
export class ToggleButtonComponent {
  buttonSelected = 'EnSerie';
  @Output() valueChange = new EventEmitter<string>();
  
  ngOnInit() {
    this.valueChange.emit(this.buttonSelected);
  }

  onValChange(value: string) {
    this.buttonSelected = value;
    this.valueChange.emit(value);
  }
}
