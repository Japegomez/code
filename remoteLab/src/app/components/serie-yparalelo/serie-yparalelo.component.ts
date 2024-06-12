import { NgClass } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DynamicTableComponent } from '../dynamic-table/dynamic-table.component';
import { CameraViewerComponent } from '../camera-viewer/camera-viewer.component';

@Component({
  selector: 'app-serie-yparalelo',
  standalone: true,
  imports: [FormsModule, NgClass, DynamicTableComponent, CameraViewerComponent],
  templateUrl: './serie-yparalelo.component.html',
  styleUrl: './serie-yparalelo.component.css'
})
export class SerieYParaleloComponent {
  nombresColumnas = ["D1", "D2", "D3", "R1", "Rama1","Rama2","Rama3","Total"];
  tensionData = [0,0,0,0,0,0,0,0];
  intensidadData = [0,0,0,0,0,0,0,0];
  valorR1: number | undefined;
  isCorrect: boolean = false;

  checkValues() {
    if (this.valorR1 === 100 || this.valorR1 === 300) {
      this.isCorrect = true;
    } else {
      this.isCorrect = false;
    }
  }
}
