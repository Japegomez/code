import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-en-serie',
  standalone: true,
  imports: [FormsModule, NgClass],
  templateUrl: './en-serie.component.html',
  styleUrl: './en-serie.component.css'
})
export class EnSerieComponent {
  numDiodosEnSerie = "1diodo";

  valorR1: number | undefined;
  isCorrect: boolean = false;

  sendSignals() {
    this.checkValues();
  }
  checkValues() {
    if (this.valorR1 === 100 || this.valorR1 === 300) {
      this.isCorrect = true;
    } else {
      this.isCorrect = false;
    }
  }
}
