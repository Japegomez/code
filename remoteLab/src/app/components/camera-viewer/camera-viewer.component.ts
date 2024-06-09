import { Component, OnDestroy, OnInit } from '@angular/core';
import { DomSanitizer, SafeUrl } from '@angular/platform-browser';
import { APIService } from '../../services/api.service';

@Component({
  selector: 'app-camera-viewer',
  templateUrl: './camera-viewer.component.html',
  styleUrls: ['./camera-viewer.component.css'],
  standalone: true,
  imports: []
})
export class CameraViewerComponent implements OnInit, OnDestroy {
  imageUrl: SafeUrl | null = null;
  imageId: string | null = null;
  interval?: number;
  constructor(private apiService: APIService, private sanitizer: DomSanitizer) { }

  ngOnInit(): void {
    this.loadImage();
    this.interval = setInterval(() => {
      this.loadImage();
    }, 1000);
  }
  ngOnDestroy(): void {
    if(this.interval){
      clearInterval(this.interval)
    }
  }
  
  loadImage(): void {
    this.apiService.getImage().subscribe((response: { image: Blob | MediaSource; id: string | null; }) => {
      const url = URL.createObjectURL(response.image);
      this.imageUrl = this.sanitizer.bypassSecurityTrustUrl(url);
      this.imageId = response.id;
    });
  }
}
