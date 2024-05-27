// dynamic-table.component.ts
import { NgFor } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dynamic-table',
  templateUrl: './dynamic-table.component.html',
  styleUrls: ['./dynamic-table.component.css'],
  standalone: true,
  imports: [NgFor]
})
export class DynamicTableComponent {
  @Input() columns: string[] | undefined;
  @Input() tensionData: number[] | undefined;
  @Input() intensidadData: number[] | undefined;
}
