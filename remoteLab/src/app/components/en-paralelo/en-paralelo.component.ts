import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DynamicTableComponent } from '../dynamic-table/dynamic-table.component';

@Component({
  selector: 'app-en-paralelo',
  standalone: true,
  imports: [FormsModule,NgClass, DynamicTableComponent],
  templateUrl: './en-paralelo.component.html',
  styleUrl: './en-paralelo.component.css'
})
export class EnParaleloComponent {
  _numRamasEnParalelo = '2ramas';

  nombresColumnas = ["D1", "D2", "R1", "R2", "Rama1","Rama2","Total"];
  tensionData = [0,0,0,0,0,0,0];
  intensidadData = [0,0,0,0,0,0,0];
  valorR1: number | undefined;
  valorR2: number | undefined;
  valorR3: number | undefined;
  isCorrect: boolean = false;

  get numRamasEnParalelo() {
    return this._numRamasEnParalelo;
  }
  
  set numRamasEnParalelo(value: string) {
    this._numRamasEnParalelo = value;
    this.updateNombresColumnas();
    this.updateTensionData();
    this.updateIntensidadData();
  }

  updateNombresColumnas() {
  if (this._numRamasEnParalelo === '2ramas') {
    this.nombresColumnas = ["D1", "D2", "R1", "R2", "Rama 1","Rama 2","Total"];
  } 
  else {
    this.nombresColumnas = ["D1", "D2","D3", "R1", "R2","R3", "Rama1","Rama2","Rama3","Total"];
  }
  }

  updateTensionData() {
    if (this._numRamasEnParalelo === "2ramas") {
      this.tensionData = [0,0,0,0,0,0,0];
    }
    else {
      this.tensionData = [0,0,0,0,0,0,0,0,0,0];
    }
  }

  updateIntensidadData() {
    if (this._numRamasEnParalelo === "2ramas") {
      this.intensidadData = [0,0,0,0,0,0,0];
    }
    else {
      this.intensidadData = [0,0,0,0,0,0,0,0,0,0];
    }
  }

  checkValues() {
    if (this._numRamasEnParalelo === '2ramas') {
      if ((this.valorR1 === 100 || this.valorR1 === 300) && (this.valorR2 === 100 || this.valorR2 === 300)) {
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    } else if (this._numRamasEnParalelo === '3ramas') {
      if ((this.valorR1 === 100 || this.valorR1 === 300) && (this.valorR2 === 100 || this.valorR2 === 300) && (this.valorR3 === 100 || this.valorR3 === 300)) {
        this.isCorrect = true;
      } else {
        this.isCorrect = false;
      }
    }
  }
}
