import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { APIService } from '../../services/api.service';
import { DynamicTableComponent } from '../dynamic-table/dynamic-table.component';

@Component({
  selector: 'app-en-serie',
  standalone: true,
  imports: [FormsModule, NgClass, DynamicTableComponent],
  templateUrl: './en-serie.component.html',
  styleUrl: './en-serie.component.css'
})
export class EnSerieComponent {
  _numDiodosEnSerie = "1diodo";

  nombresColumnas = ["D1","R1","Total"];
  tensionData = [0,0,0];
  intensidadData = [0,0,0];
  valorR1: number | undefined;
  isCorrect: boolean = false;


  constructor(private apiService: APIService) {
  }


  get numDiodosEnSerie(): string {
    return this._numDiodosEnSerie;
  }

  set numDiodosEnSerie(value: string) {
    this._numDiodosEnSerie = value
    this.updateNombresColumnas()
    this.updateTensionData()
    this.updateIntensidadData()
  }

  updateNombresColumnas() {
  if (this._numDiodosEnSerie === "2diodos") {
    this.nombresColumnas = ["D1", "D2", "R1", "Total"];
  } 
  else if (this._numDiodosEnSerie === "3diodos") {
    this.nombresColumnas = ["D1", "D2", "D3", "R1", "Total"];
  }
  else {
    this.nombresColumnas = ["D1", "R1", "Total"];
  }
  }

  updateTensionData() {
    if (this._numDiodosEnSerie === "1diodo") {
      this.tensionData = [0,0,0];
    }
    else if (this._numDiodosEnSerie === "2diodos") {
      this.tensionData = [0,0,0,0];
    }
    else {
      this.tensionData = [0,0,0,0,0];
    }
  }

  updateIntensidadData() {
    if (this._numDiodosEnSerie === "1diodo") {
      this.intensidadData = [0,0,0];
    }
    else if (this._numDiodosEnSerie === "2diodos") {
      this.intensidadData = [0,0,0,0];
    }
    else {
      this.intensidadData = [0,0,0,0,0];
    }
  }

  
  myFunction() {
    // this.apiService.runLabConfig("EnSerie", 1)
  }
  checkValues() {
    if (this.valorR1 === 100 || this.valorR1 === 300) {
      this.isCorrect = true;
    } else {
      this.isCorrect = false;
    }
  }
}
