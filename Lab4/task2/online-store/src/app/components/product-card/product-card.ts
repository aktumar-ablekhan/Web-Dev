import { Component, input } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-card.html',
  styleUrls: ['./product-card.css'],
})
export class ProductCard {
  product = input<any>();

  stars(): number[] {
    return [1, 2, 3, 4, 5];
  }

  roundedRating(): number {
  const p = this.product();
  return Math.round(p?.rating ?? 0);
 }

  shareTelegram(): void {
    const p = this.product();
    const url =
      'https://t.me/share/url?url=' +
      encodeURIComponent(p.link) +
      '&text=' +
      encodeURIComponent(p.name);
    window.open(url, '_blank');
  }

  shareWhatsapp(): void {
    const p = this.product();
    const text = 'Check out this product: ' + p.link;
    const url = 'https://wa.me/?text=' + encodeURIComponent(text);
    window.open(url, '_blank');
  }
}
