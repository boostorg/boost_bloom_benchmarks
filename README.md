# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.46</td>
    <td align="right">5.92</td>
    <td align="right">4.28</td>
    <td align="right">7.16</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.03</td>
    <td align="right">12.05</td>
    <td align="right">18.12</td>
    <td align="right">19.57</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.48</td>
    <td align="right">5.13</td>
    <td align="right">5.13</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.55</td>
    <td align="right">17.90</td>
    <td align="right">19.27</td>
    <td align="right">21.62</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.40</td>
    <td align="right">5.17</td>
    <td align="right">5.17</td>
    <td align="right">5.17</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.37</td>
    <td align="right">21.61</td>
    <td align="right">18.16</td>
    <td align="right">22.17</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="right">5.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.57</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.36</td>
    <td align="right">27.72</td>
    <td align="right">18.55</td>
    <td align="right">23.17</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
    <td align="right">6.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.65</td>
    <td align="right">5.65</td>
    <td align="right">5.65</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.52</td>
    <td align="right">6.97</td>
    <td align="right">6.96</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.23</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.88</td>
    <td align="right">9.28</td>
    <td align="right">9.28</td>
    <td align="right">9.28</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.03</td>
    <td align="right">9.66</td>
    <td align="right">9.66</td>
    <td align="right">9.67</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.72</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.15</td>
    <td align="right">11.79</td>
    <td align="right">11.79</td>
    <td align="right">11.79</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.06</td>
    <td align="right">13.63</td>
    <td align="right">13.64</td>
    <td align="right">13.64</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.81</td>
    <td align="right">5.85</td>
    <td align="right">4.17</td>
    <td align="right">6.62</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.40</td>
    <td align="right">12.73</td>
    <td align="right">12.73</td>
    <td align="right">12.73</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.60</td>
    <td align="right">15.09</td>
    <td align="right">15.11</td>
    <td align="right">15.12</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.83</td>
    <td align="right">5.88</td>
    <td align="right">4.17</td>
    <td align="right">6.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.19</td>
    <td align="right">2.79</td>
    <td align="right">2.79</td>
    <td align="right">2.80</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.66</td>
    <td align="right">4.80</td>
    <td align="right">4.82</td>
    <td align="right">4.78</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.31</td>
    <td align="right">2.84</td>
    <td align="right">2.85</td>
    <td align="right">2.84</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.48</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.79</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.65</td>
    <td align="right">3.93</td>
    <td align="right">6.66</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.62</td>
    <td align="right">8.23</td>
    <td align="right">6.20</td>
    <td align="right">8.74</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.82</td>
    <td align="right">7.99</td>
    <td align="right">6.16</td>
    <td align="right">8.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">5.69</td>
    <td align="right">3.91</td>
    <td align="right">6.40</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.46</td>
    <td align="right">9.43</td>
    <td align="right">6.28</td>
    <td align="right">8.96</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.64</td>
    <td align="right">9.21</td>
    <td align="right">6.24</td>
    <td align="right">8.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">7.33</td>
    <td align="right">14.46</td>
    <td align="right">15.75</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">8.82</td>
    <td align="right">18.88</td>
    <td align="right">19.44</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.36</td>
    <td align="right">11.23</td>
    <td align="right">11.25</td>
    <td align="right">11.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.39</td>
    <td align="right">14.38</td>
    <td align="right">16.74</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.53</td>
    <td align="right">10.53</td>
    <td align="right">16.16</td>
    <td align="right">18.32</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.00</td>
    <td align="right">14.32</td>
    <td align="right">14.35</td>
    <td align="right">14.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.67</td>
    <td align="right">11.94</td>
    <td align="right">14.07</td>
    <td align="right">16.89</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.96</td>
    <td align="right">12.95</td>
    <td align="right">17.32</td>
    <td align="right">20.09</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.45</td>
    <td align="right">16.28</td>
    <td align="right">16.25</td>
    <td align="right">16.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.85</td>
    <td align="right">14.36</td>
    <td align="right">14.76</td>
    <td align="right">17.99</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.63</td>
    <td align="right">15.17</td>
    <td align="right">16.92</td>
    <td align="right">19.77</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.82</td>
    <td align="right">21.21</td>
    <td align="right">21.14</td>
    <td align="right">21.29</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">57.90</td>
    <td align="right">22.87</td>
    <td align="right">14.67</td>
    <td align="right">21.39</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.40</td>
    <td align="right">17.18</td>
    <td align="right">21.01</td>
    <td align="right">22.53</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.04</td>
    <td align="right">5.67</td>
    <td align="right">5.65</td>
    <td align="right">5.63</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.31</td>
    <td align="right">5.97</td>
    <td align="right">5.98</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">52.20</td>
    <td align="right">57.42</td>
    <td align="right">28.83</td>
    <td align="right">33.49</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.45</td>
    <td align="right">12.50</td>
    <td align="right">12.56</td>
    <td align="right">12.47</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">12.07</td>
    <td align="right">12.59</td>
    <td align="right">12.59</td>
    <td align="right">12.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.91</td>
    <td align="right">95.79</td>
    <td align="right">34.35</td>
    <td align="right">43.78</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.94</td>
    <td align="right">18.74</td>
    <td align="right">18.73</td>
    <td align="right">18.72</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.20</td>
    <td align="right">19.38</td>
    <td align="right">19.37</td>
    <td align="right">19.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.99</td>
    <td align="right">136.63</td>
    <td align="right">40.00</td>
    <td align="right">54.53</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.76</td>
    <td align="right">22.40</td>
    <td align="right">22.40</td>
    <td align="right">22.38</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">23.06</td>
    <td align="right">25.67</td>
    <td align="right">25.67</td>
    <td align="right">25.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.20</td>
    <td align="right">6.93</td>
    <td align="right">6.91</td>
    <td align="right">6.90</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.98</td>
    <td align="right">8.73</td>
    <td align="right">8.72</td>
    <td align="right">8.75</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.26</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.54</td>
    <td align="right">17.01</td>
    <td align="right">17.02</td>
    <td align="right">17.03</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.59</td>
    <td align="right">22.15</td>
    <td align="right">22.21</td>
    <td align="right">22.10</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.09</td>
    <td align="right">8.41</td>
    <td align="right">8.42</td>
    <td align="right">8.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.76</td>
    <td align="right">31.32</td>
    <td align="right">31.29</td>
    <td align="right">31.29</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.49</td>
    <td align="right">35.18</td>
    <td align="right">35.16</td>
    <td align="right">35.16</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.46</td>
    <td align="right">21.14</td>
    <td align="right">15.17</td>
    <td align="right">16.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.30</td>
    <td align="right">39.43</td>
    <td align="right">39.43</td>
    <td align="right">39.45</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.98</td>
    <td align="right">52.28</td>
    <td align="right">51.49</td>
    <td align="right">52.16</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">21.92</td>
    <td align="right">24.21</td>
    <td align="right">17.10</td>
    <td align="right">18.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.34</td>
    <td align="right">4.01</td>
    <td align="right">4.00</td>
    <td align="right">4.02</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.96</td>
    <td align="right">7.39</td>
    <td align="right">7.48</td>
    <td align="right">7.41</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.87</td>
    <td align="right">5.85</td>
    <td align="right">5.85</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.88</td>
    <td align="right">8.75</td>
    <td align="right">8.77</td>
    <td align="right">8.74</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.69</td>
    <td align="right">9.66</td>
    <td align="right">9.72</td>
    <td align="right">9.69</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.26</td>
    <td align="right">12.49</td>
    <td align="right">12.48</td>
    <td align="right">12.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.94</td>
    <td align="right">20.93</td>
    <td align="right">14.90</td>
    <td align="right">16.43</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.21</td>
    <td align="right">26.82</td>
    <td align="right">21.99</td>
    <td align="right">23.32</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.97</td>
    <td align="right">27.41</td>
    <td align="right">22.21</td>
    <td align="right">23.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.62</td>
    <td align="right">24.21</td>
    <td align="right">16.72</td>
    <td align="right">18.43</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">30.99</td>
    <td align="right">37.48</td>
    <td align="right">25.27</td>
    <td align="right">26.90</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">30.44</td>
    <td align="right">37.40</td>
    <td align="right">25.38</td>
    <td align="right">26.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.27</td>
    <td align="right">9.21</td>
    <td align="right">16.05</td>
    <td align="right">17.80</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.49</td>
    <td align="right">10.04</td>
    <td align="right">20.31</td>
    <td align="right">21.25</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.10</td>
    <td align="right">15.21</td>
    <td align="right">15.26</td>
    <td align="right">15.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.00</td>
    <td align="right">17.87</td>
    <td align="right">18.36</td>
    <td align="right">21.24</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.85</td>
    <td align="right">22.82</td>
    <td align="right">22.12</td>
    <td align="right">24.50</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.46</td>
    <td align="right">31.95</td>
    <td align="right">31.99</td>
    <td align="right">31.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.48</td>
    <td align="right">29.03</td>
    <td align="right">22.33</td>
    <td align="right">27.03</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.97</td>
    <td align="right">34.60</td>
    <td align="right">26.73</td>
    <td align="right">32.18</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.35</td>
    <td align="right">50.15</td>
    <td align="right">50.14</td>
    <td align="right">50.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.78</td>
    <td align="right">43.70</td>
    <td align="right">25.31</td>
    <td align="right">32.06</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.29</td>
    <td align="right">52.03</td>
    <td align="right">29.21</td>
    <td align="right">34.86</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">69.93</td>
    <td align="right">74.25</td>
    <td align="right">74.10</td>
    <td align="right">74.15</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.13</td>
    <td align="right">6.12</td>
    <td align="right">4.68</td>
    <td align="right">7.13</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.44</td>
    <td align="right">10.91</td>
    <td align="right">17.44</td>
    <td align="right">18.72</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.05</td>
    <td align="right">4.08</td>
    <td align="right">4.07</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.06</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.66</td>
    <td align="right">16.07</td>
    <td align="right">18.57</td>
    <td align="right">21.53</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="right">4.70</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.26</td>
    <td align="right">5.27</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.10</td>
    <td align="right">20.00</td>
    <td align="right">17.60</td>
    <td align="right">21.22</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.28</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.92</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.86</td>
    <td align="right">23.98</td>
    <td align="right">18.24</td>
    <td align="right">22.62</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">5.74</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.46</td>
    <td align="right">3.46</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.26</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.35</td>
    <td align="right">3.70</td>
    <td align="right">3.69</td>
    <td align="right">3.71</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.87</td>
    <td align="right">2.67</td>
    <td align="right">2.69</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.38</td>
    <td align="right">4.80</td>
    <td align="right">4.80</td>
    <td align="right">4.80</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.03</td>
    <td align="right">4.94</td>
    <td align="right">4.94</td>
    <td align="right">4.94</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.83</td>
    <td align="right">7.73</td>
    <td align="right">7.71</td>
    <td align="right">7.71</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.96</td>
    <td align="right">7.45</td>
    <td align="right">7.41</td>
    <td align="right">7.41</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.39</td>
    <td align="right">4.46</td>
    <td align="right">3.34</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.19</td>
    <td align="right">8.23</td>
    <td align="right">8.23</td>
    <td align="right">8.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.97</td>
    <td align="right">8.34</td>
    <td align="right">8.35</td>
    <td align="right">8.36</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.44</td>
    <td align="right">4.50</td>
    <td align="right">3.33</td>
    <td align="right">5.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.84</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.06</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.96</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">3.88</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.27</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.46</td>
    <td align="right">4.21</td>
    <td align="right">3.17</td>
    <td align="right">5.68</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.82</td>
    <td align="right">6.35</td>
    <td align="right">5.23</td>
    <td align="right">7.69</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">5.96</td>
    <td align="right">6.04</td>
    <td align="right">4.86</td>
    <td align="right">7.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.49</td>
    <td align="right">4.22</td>
    <td align="right">3.13</td>
    <td align="right">5.69</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.93</td>
    <td align="right">7.24</td>
    <td align="right">5.21</td>
    <td align="right">7.87</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.22</td>
    <td align="right">7.02</td>
    <td align="right">5.04</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.33</td>
    <td align="right">6.65</td>
    <td align="right">13.72</td>
    <td align="right">15.42</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.89</td>
    <td align="right">18.14</td>
    <td align="right">18.87</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.25</td>
    <td align="right">10.39</td>
    <td align="right">10.41</td>
    <td align="right">10.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.55</td>
    <td align="right">9.06</td>
    <td align="right">13.42</td>
    <td align="right">15.57</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">9.27</td>
    <td align="right">15.38</td>
    <td align="right">17.71</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.79</td>
    <td align="right">14.57</td>
    <td align="right">14.58</td>
    <td align="right">14.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.96</td>
    <td align="right">10.65</td>
    <td align="right">13.22</td>
    <td align="right">15.53</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.48</td>
    <td align="right">11.99</td>
    <td align="right">16.39</td>
    <td align="right">18.95</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.61</td>
    <td align="right">15.77</td>
    <td align="right">15.81</td>
    <td align="right">15.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.31</td>
    <td align="right">13.36</td>
    <td align="right">14.00</td>
    <td align="right">17.00</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.12</td>
    <td align="right">13.61</td>
    <td align="right">15.78</td>
    <td align="right">18.75</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.81</td>
    <td align="right">21.06</td>
    <td align="right">21.02</td>
    <td align="right">20.98</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">51.97</td>
    <td align="right">23.00</td>
    <td align="right">14.61</td>
    <td align="right">21.18</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.00</td>
    <td align="right">15.48</td>
    <td align="right">20.32</td>
    <td align="right">21.79</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.73</td>
    <td align="right">4.73</td>
    <td align="right">4.70</td>
    <td align="right">4.69</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.64</td>
    <td align="right">6.25</td>
    <td align="right">6.23</td>
    <td align="right">6.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.79</td>
    <td align="right">49.35</td>
    <td align="right">26.32</td>
    <td align="right">31.11</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.49</td>
    <td align="right">11.45</td>
    <td align="right">11.46</td>
    <td align="right">11.47</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.70</td>
    <td align="right">12.80</td>
    <td align="right">12.81</td>
    <td align="right">12.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.52</td>
    <td align="right">87.04</td>
    <td align="right">31.84</td>
    <td align="right">40.27</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.14</td>
    <td align="right">18.24</td>
    <td align="right">18.23</td>
    <td align="right">18.25</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.03</td>
    <td align="right">18.96</td>
    <td align="right">18.96</td>
    <td align="right">18.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">119.92</td>
    <td align="right">119.60</td>
    <td align="right">36.84</td>
    <td align="right">52.66</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.16</td>
    <td align="right">22.00</td>
    <td align="right">22.00</td>
    <td align="right">22.02</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.02</td>
    <td align="right">15.27</td>
    <td align="right">15.27</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">5.27</td>
    <td align="right">6.18</td>
    <td align="right">6.18</td>
    <td align="right">6.20</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.50</td>
    <td align="right">4.98</td>
    <td align="right">5.00</td>
    <td align="right">5.01</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.14</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.73</td>
    <td align="right">10.49</td>
    <td align="right">10.48</td>
    <td align="right">10.46</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.55</td>
    <td align="right">12.13</td>
    <td align="right">12.13</td>
    <td align="right">12.08</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.94</td>
    <td align="right">7.63</td>
    <td align="right">7.64</td>
    <td align="right">7.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">18.48</td>
    <td align="right">22.46</td>
    <td align="right">22.46</td>
    <td align="right">22.46</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">17.81</td>
    <td align="right">22.51</td>
    <td align="right">22.48</td>
    <td align="right">22.50</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.25</td>
    <td align="right">16.61</td>
    <td align="right">12.59</td>
    <td align="right">13.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.02</td>
    <td align="right">29.67</td>
    <td align="right">29.71</td>
    <td align="right">29.71</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.11</td>
    <td align="right">30.94</td>
    <td align="right">30.96</td>
    <td align="right">30.98</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.95</td>
    <td align="right">18.48</td>
    <td align="right">13.96</td>
    <td align="right">15.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.68</td>
    <td align="right">3.45</td>
    <td align="right">3.42</td>
    <td align="right">3.39</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.19</td>
    <td align="right">5.56</td>
    <td align="right">5.57</td>
    <td align="right">5.59</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.22</td>
    <td align="right">5.39</td>
    <td align="right">5.37</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.90</td>
    <td align="right">7.93</td>
    <td align="right">7.99</td>
    <td align="right">7.92</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.32</td>
    <td align="right">9.97</td>
    <td align="right">9.97</td>
    <td align="right">9.99</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.96</td>
    <td align="right">12.42</td>
    <td align="right">12.43</td>
    <td align="right">12.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.44</td>
    <td align="right">16.40</td>
    <td align="right">12.03</td>
    <td align="right">13.44</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.44</td>
    <td align="right">21.68</td>
    <td align="right">17.18</td>
    <td align="right">19.06</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.27</td>
    <td align="right">21.52</td>
    <td align="right">17.03</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">15.88</td>
    <td align="right">18.32</td>
    <td align="right">13.35</td>
    <td align="right">15.19</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">24.18</td>
    <td align="right">29.36</td>
    <td align="right">18.90</td>
    <td align="right">21.11</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">24.52</td>
    <td align="right">26.84</td>
    <td align="right">18.96</td>
    <td align="right">20.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.46</td>
    <td align="right">7.85</td>
    <td align="right">15.05</td>
    <td align="right">17.13</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.93</td>
    <td align="right">10.03</td>
    <td align="right">19.77</td>
    <td align="right">20.99</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.53</td>
    <td align="right">13.34</td>
    <td align="right">13.37</td>
    <td align="right">13.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.93</td>
    <td align="right">17.17</td>
    <td align="right">18.34</td>
    <td align="right">21.21</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.02</td>
    <td align="right">19.22</td>
    <td align="right">19.54</td>
    <td align="right">22.44</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">32.32</td>
    <td align="right">34.01</td>
    <td align="right">34.01</td>
    <td align="right">33.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.47</td>
    <td align="right">27.26</td>
    <td align="right">21.68</td>
    <td align="right">25.51</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.97</td>
    <td align="right">33.58</td>
    <td align="right">24.96</td>
    <td align="right">29.48</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">44.86</td>
    <td align="right">49.30</td>
    <td align="right">49.36</td>
    <td align="right">49.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">44.02</td>
    <td align="right">36.49</td>
    <td align="right">25.43</td>
    <td align="right">32.45</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">53.64</td>
    <td align="right">41.22</td>
    <td align="right">26.37</td>
    <td align="right">32.60</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">73.24</td>
    <td align="right">70.58</td>
    <td align="right">70.14</td>
    <td align="right">70.39</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.79</td>
    <td align="right">2.60</td>
    <td align="right">1.99</td>
    <td align="right">4.31</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.36</td>
    <td align="right">4.15</td>
    <td align="right">11.38</td>
    <td align="right">11.75</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.44</td>
    <td align="right">6.09</td>
    <td align="right">12.00</td>
    <td align="right">12.86</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.63</td>
    <td align="right">7.34</td>
    <td align="right">11.22</td>
    <td align="right">12.81</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.63</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.94</td>
    <td align="right">9.30</td>
    <td align="right">11.36</td>
    <td align="right">13.41</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.78</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.22</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.25</td>
    <td align="right">1.73</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.86</td>
    <td align="right">1.85</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.71</td>
    <td align="right">2.15</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.09</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.96</td>
    <td align="right">2.42</td>
    <td align="right">1.76</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.69</td>
    <td align="right">3.38</td>
    <td align="right">3.38</td>
    <td align="right">3.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">3.58</td>
    <td align="right">3.57</td>
    <td align="right">3.57</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.96</td>
    <td align="right">2.93</td>
    <td align="right">1.73</td>
    <td align="right">3.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.00</td>
    <td align="right">1.69</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.30</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.33</td>
    <td align="right">1.75</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.03</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.82</td>
    <td align="right">2.16</td>
    <td align="right">2.15</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.93</td>
    <td align="right">2.39</td>
    <td align="right">1.75</td>
    <td align="right">3.88</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.12</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.03</td>
    <td align="right">3.03</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.98</td>
    <td align="right">2.90</td>
    <td align="right">1.76</td>
    <td align="right">3.86</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.52</td>
    <td align="right">3.38</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.66</td>
    <td align="right">3.61</td>
    <td align="right">3.60</td>
    <td align="right">3.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.24</td>
    <td align="right">3.27</td>
    <td align="right">10.25</td>
    <td align="right">10.86</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.95</td>
    <td align="right">3.95</td>
    <td align="right">12.74</td>
    <td align="right">12.97</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.73</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.38</td>
    <td align="right">4.36</td>
    <td align="right">9.96</td>
    <td align="right">11.13</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.41</td>
    <td align="right">4.50</td>
    <td align="right">10.50</td>
    <td align="right">11.97</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.85</td>
    <td align="right">6.77</td>
    <td align="right">6.77</td>
    <td align="right">6.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.48</td>
    <td align="right">5.27</td>
    <td align="right">9.74</td>
    <td align="right">10.95</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.49</td>
    <td align="right">5.75</td>
    <td align="right">11.28</td>
    <td align="right">12.99</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.09</td>
    <td align="right">7.56</td>
    <td align="right">7.56</td>
    <td align="right">7.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">6.99</td>
    <td align="right">6.29</td>
    <td align="right">10.21</td>
    <td align="right">11.72</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">6.37</td>
    <td align="right">10.73</td>
    <td align="right">12.66</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.13</td>
    <td align="right">10.60</td>
    <td align="right">10.62</td>
    <td align="right">10.60</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.58</td>
    <td align="right">11.60</td>
    <td align="right">6.35</td>
    <td align="right">9.57</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.84</td>
    <td align="right">6.33</td>
    <td align="right">13.07</td>
    <td align="right">13.65</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.12</td>
    <td align="right">2.07</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.18</td>
    <td align="right">2.10</td>
    <td align="right">2.09</td>
    <td align="right">2.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.12</td>
    <td align="right">11.56</td>
    <td align="right">16.21</td>
    <td align="right">17.94</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.75</td>
    <td align="right">3.82</td>
    <td align="right">3.57</td>
    <td align="right">3.92</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.48</td>
    <td align="right">3.24</td>
    <td align="right">3.19</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.85</td>
    <td align="right">25.68</td>
    <td align="right">18.28</td>
    <td align="right">22.44</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.19</td>
    <td align="right">6.65</td>
    <td align="right">6.41</td>
    <td align="right">6.58</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.78</td>
    <td align="right">6.16</td>
    <td align="right">6.13</td>
    <td align="right">6.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.59</td>
    <td align="right">39.04</td>
    <td align="right">20.54</td>
    <td align="right">27.09</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.40</td>
    <td align="right">8.05</td>
    <td align="right">8.11</td>
    <td align="right">7.94</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.73</td>
    <td align="right">6.32</td>
    <td align="right">6.83</td>
    <td align="right">6.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.75</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.77</td>
    <td align="right">2.68</td>
    <td align="right">2.69</td>
    <td align="right">2.67</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.44</td>
    <td align="right">2.62</td>
    <td align="right">2.66</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.11</td>
    <td align="right">4.24</td>
    <td align="right">4.55</td>
    <td align="right">4.35</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.34</td>
    <td align="right">4.66</td>
    <td align="right">4.54</td>
    <td align="right">4.60</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.68</td>
    <td align="right">3.31</td>
    <td align="right">3.33</td>
    <td align="right">3.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.25</td>
    <td align="right">9.42</td>
    <td align="right">9.30</td>
    <td align="right">10.01</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.16</td>
    <td align="right">9.82</td>
    <td align="right">10.07</td>
    <td align="right">9.91</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.25</td>
    <td align="right">8.07</td>
    <td align="right">5.90</td>
    <td align="right">6.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.14</td>
    <td align="right">12.81</td>
    <td align="right">12.90</td>
    <td align="right">12.86</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.87</td>
    <td align="right">13.62</td>
    <td align="right">13.61</td>
    <td align="right">13.90</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">10.31</td>
    <td align="right">11.20</td>
    <td align="right">6.69</td>
    <td align="right">7.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.40</td>
    <td align="right">2.57</td>
    <td align="right">2.62</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.79</td>
    <td align="right">2.65</td>
    <td align="right">2.67</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.76</td>
    <td align="right">2.67</td>
    <td align="right">2.70</td>
    <td align="right">2.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">3.27</td>
    <td align="right">3.14</td>
    <td align="right">3.11</td>
    <td align="right">3.36</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.08</td>
    <td align="right">4.64</td>
    <td align="right">4.36</td>
    <td align="right">4.39</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.36</td>
    <td align="right">4.78</td>
    <td align="right">4.93</td>
    <td align="right">4.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.87</td>
    <td align="right">8.12</td>
    <td align="right">6.03</td>
    <td align="right">6.68</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.78</td>
    <td align="right">9.01</td>
    <td align="right">9.01</td>
    <td align="right">9.58</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.18</td>
    <td align="right">9.98</td>
    <td align="right">10.05</td>
    <td align="right">10.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">10.28</td>
    <td align="right">10.90</td>
    <td align="right">6.43</td>
    <td align="right">7.91</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.65</td>
    <td align="right">12.84</td>
    <td align="right">13.19</td>
    <td align="right">12.87</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">15.83</td>
    <td align="right">13.80</td>
    <td align="right">13.05</td>
    <td align="right">12.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.71</td>
    <td align="right">4.40</td>
    <td align="right">11.49</td>
    <td align="right">12.49</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">9.07</td>
    <td align="right">5.03</td>
    <td align="right">13.73</td>
    <td align="right">14.25</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.10</td>
    <td align="right">7.06</td>
    <td align="right">7.05</td>
    <td align="right">7.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">9.22</td>
    <td align="right">8.50</td>
    <td align="right">12.67</td>
    <td align="right">15.09</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">13.27</td>
    <td align="right">8.10</td>
    <td align="right">13.37</td>
    <td align="right">15.47</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.73</td>
    <td align="right">12.49</td>
    <td align="right">12.21</td>
    <td align="right">12.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">16.66</td>
    <td align="right">13.68</td>
    <td align="right">14.34</td>
    <td align="right">16.94</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">24.53</td>
    <td align="right">16.40</td>
    <td align="right">16.90</td>
    <td align="right">20.26</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">27.25</td>
    <td align="right">23.91</td>
    <td align="right">23.51</td>
    <td align="right">24.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">22.15</td>
    <td align="right">16.19</td>
    <td align="right">15.03</td>
    <td align="right">18.30</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.21</td>
    <td align="right">19.06</td>
    <td align="right">16.37</td>
    <td align="right">20.16</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.60</td>
    <td align="right">35.50</td>
    <td align="right">35.49</td>
    <td align="right">35.50</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.24</td>
    <td align="right">5.17</td>
    <td align="right">3.62</td>
    <td align="right">5.91</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.29</td>
    <td align="right">11.32</td>
    <td align="right">14.16</td>
    <td align="right">15.25</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.58</td>
    <td align="right">3.56</td>
    <td align="right">3.58</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.34</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.03</td>
    <td align="right">16.22</td>
    <td align="right">15.37</td>
    <td align="right">16.84</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.44</td>
    <td align="right">4.00</td>
    <td align="right">3.97</td>
    <td align="right">3.97</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">4.79</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">49.29</td>
    <td align="right">20.41</td>
    <td align="right">14.12</td>
    <td align="right">16.90</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">7.52</td>
    <td align="right">4.37</td>
    <td align="right">4.35</td>
    <td align="right">4.33</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">9.74</td>
    <td align="right">5.09</td>
    <td align="right">5.07</td>
    <td align="right">5.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">26.19</td>
    <td align="right">25.02</td>
    <td align="right">14.38</td>
    <td align="right">17.68</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">11.55</td>
    <td align="right">4.71</td>
    <td align="right">4.70</td>
    <td align="right">4.69</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">12.83</td>
    <td align="right">5.60</td>
    <td align="right">5.58</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.37</td>
    <td align="right">4.30</td>
    <td align="right">4.32</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.46</td>
    <td align="right">4.63</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.84</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.30</td>
    <td align="right">6.99</td>
    <td align="right">6.91</td>
    <td align="right">6.91</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.79</td>
    <td align="right">7.17</td>
    <td align="right">7.14</td>
    <td align="right">7.16</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.81</td>
    <td align="right">2.98</td>
    <td align="right">2.36</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">16.63</td>
    <td align="right">9.06</td>
    <td align="right">9.06</td>
    <td align="right">9.07</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">18.63</td>
    <td align="right">10.51</td>
    <td align="right">10.53</td>
    <td align="right">10.41</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.29</td>
    <td align="right">4.40</td>
    <td align="right">3.09</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">20.95</td>
    <td align="right">10.41</td>
    <td align="right">10.31</td>
    <td align="right">10.18</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.98</td>
    <td align="right">12.15</td>
    <td align="right">12.07</td>
    <td align="right">12.07</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">7.83</td>
    <td align="right">4.46</td>
    <td align="right">3.11</td>
    <td align="right">4.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.80</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.79</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.23</td>
    <td align="right">3.41</td>
    <td align="right">2.69</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.88</td>
    <td align="right">3.28</td>
    <td align="right">4.97</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">4.57</td>
    <td align="right">3.91</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">8.48</td>
    <td align="right">4.31</td>
    <td align="right">3.00</td>
    <td align="right">4.82</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.93</td>
    <td align="right">6.41</td>
    <td align="right">5.04</td>
    <td align="right">6.80</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.67</td>
    <td align="right">6.23</td>
    <td align="right">4.95</td>
    <td align="right">6.61</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">13.15</td>
    <td align="right">4.34</td>
    <td align="right">3.03</td>
    <td align="right">5.16</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.80</td>
    <td align="right">6.98</td>
    <td align="right">5.09</td>
    <td align="right">6.89</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">20.01</td>
    <td align="right">6.84</td>
    <td align="right">5.11</td>
    <td align="right">6.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.02</td>
    <td align="right">6.70</td>
    <td align="right">11.32</td>
    <td align="right">12.45</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.04</td>
    <td align="right">8.92</td>
    <td align="right">14.03</td>
    <td align="right">14.58</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.01</td>
    <td align="right">8.89</td>
    <td align="right">9.06</td>
    <td align="right">9.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.43</td>
    <td align="right">9.85</td>
    <td align="right">11.88</td>
    <td align="right">13.55</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.88</td>
    <td align="right">11.18</td>
    <td align="right">13.12</td>
    <td align="right">14.74</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.68</td>
    <td align="right">12.87</td>
    <td align="right">12.90</td>
    <td align="right">12.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">16.93</td>
    <td align="right">11.36</td>
    <td align="right">11.86</td>
    <td align="right">13.82</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.13</td>
    <td align="right">13.20</td>
    <td align="right">12.67</td>
    <td align="right">14.71</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">29.97</td>
    <td align="right">15.28</td>
    <td align="right">15.31</td>
    <td align="right">15.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">23.96</td>
    <td align="right">13.59</td>
    <td align="right">12.31</td>
    <td align="right">14.64</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.36</td>
    <td align="right">15.13</td>
    <td align="right">12.27</td>
    <td align="right">14.87</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.53</td>
    <td align="right">22.95</td>
    <td align="right">22.94</td>
    <td align="right">22.91</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">44.86</td>
    <td align="right">23.60</td>
    <td align="right">15.56</td>
    <td align="right">20.30</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.74</td>
    <td align="right">39.75</td>
    <td align="right">24.15</td>
    <td align="right">27.06</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.66</td>
    <td align="right">4.87</td>
    <td align="right">4.84</td>
    <td align="right">4.83</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.93</td>
    <td align="right">4.83</td>
    <td align="right">4.61</td>
    <td align="right">4.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">39.82</td>
    <td align="right">39.21</td>
    <td align="right">20.53</td>
    <td align="right">23.85</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">8.55</td>
    <td align="right">8.28</td>
    <td align="right">8.44</td>
    <td align="right">8.35</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">9.77</td>
    <td align="right">9.51</td>
    <td align="right">9.46</td>
    <td align="right">9.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">71.07</td>
    <td align="right">83.07</td>
    <td align="right">26.88</td>
    <td align="right">34.78</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.76</td>
    <td align="right">14.54</td>
    <td align="right">14.64</td>
    <td align="right">14.63</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.56</td>
    <td align="right">16.92</td>
    <td align="right">16.90</td>
    <td align="right">16.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.76</td>
    <td align="right">118.04</td>
    <td align="right">31.19</td>
    <td align="right">42.73</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.82</td>
    <td align="right">18.42</td>
    <td align="right">18.45</td>
    <td align="right">18.55</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.96</td>
    <td align="right">22.75</td>
    <td align="right">22.79</td>
    <td align="right">22.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">7.06</td>
    <td align="right">4.81</td>
    <td align="right">4.60</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.85</td>
    <td align="right">5.28</td>
    <td align="right">5.03</td>
    <td align="right">4.98</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.06</td>
    <td align="right">3.57</td>
    <td align="right">3.57</td>
    <td align="right">3.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.78</td>
    <td align="right">11.44</td>
    <td align="right">11.42</td>
    <td align="right">11.32</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">19.79</td>
    <td align="right">13.42</td>
    <td align="right">13.63</td>
    <td align="right">13.60</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.09</td>
    <td align="right">6.06</td>
    <td align="right">5.23</td>
    <td align="right">6.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">27.65</td>
    <td align="right">24.32</td>
    <td align="right">24.34</td>
    <td align="right">24.46</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">31.18</td>
    <td align="right">29.82</td>
    <td align="right">29.78</td>
    <td align="right">29.84</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.42</td>
    <td align="right">15.78</td>
    <td align="right">11.22</td>
    <td align="right">12.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.26</td>
    <td align="right">35.31</td>
    <td align="right">35.21</td>
    <td align="right">35.25</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.58</td>
    <td align="right">37.78</td>
    <td align="right">37.75</td>
    <td align="right">37.78</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.33</td>
    <td align="right">17.85</td>
    <td align="right">12.38</td>
    <td align="right">13.61</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.30</td>
    <td align="right">7.65</td>
    <td align="right">7.66</td>
    <td align="right">7.65</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.24</td>
    <td align="right">3.70</td>
    <td align="right">3.47</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.62</td>
    <td align="right">3.77</td>
    <td align="right">3.62</td>
    <td align="right">3.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.19</td>
    <td align="right">8.95</td>
    <td align="right">7.71</td>
    <td align="right">8.57</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.66</td>
    <td align="right">8.26</td>
    <td align="right">7.42</td>
    <td align="right">8.71</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.37</td>
    <td align="right">9.63</td>
    <td align="right">8.42</td>
    <td align="right">9.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.86</td>
    <td align="right">15.64</td>
    <td align="right">11.14</td>
    <td align="right">12.09</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.99</td>
    <td align="right">19.63</td>
    <td align="right">16.58</td>
    <td align="right">17.51</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.43</td>
    <td align="right">19.33</td>
    <td align="right">16.35</td>
    <td align="right">17.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.75</td>
    <td align="right">17.90</td>
    <td align="right">12.37</td>
    <td align="right">13.80</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.54</td>
    <td align="right">26.97</td>
    <td align="right">18.98</td>
    <td align="right">20.10</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.58</td>
    <td align="right">26.89</td>
    <td align="right">19.02</td>
    <td align="right">19.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.16</td>
    <td align="right">7.72</td>
    <td align="right">12.16</td>
    <td align="right">13.28</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.74</td>
    <td align="right">9.89</td>
    <td align="right">14.82</td>
    <td align="right">15.44</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.56</td>
    <td align="right">9.94</td>
    <td align="right">9.93</td>
    <td align="right">9.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">14.41</td>
    <td align="right">14.90</td>
    <td align="right">15.39</td>
    <td align="right">17.45</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.28</td>
    <td align="right">20.72</td>
    <td align="right">18.53</td>
    <td align="right">20.75</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">21.52</td>
    <td align="right">21.28</td>
    <td align="right">21.28</td>
    <td align="right">21.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.96</td>
    <td align="right">28.29</td>
    <td align="right">20.87</td>
    <td align="right">24.11</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.15</td>
    <td align="right">33.63</td>
    <td align="right">20.57</td>
    <td align="right">25.46</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">42.62</td>
    <td align="right">40.23</td>
    <td align="right">40.30</td>
    <td align="right">40.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">36.03</td>
    <td align="right">35.12</td>
    <td align="right">23.05</td>
    <td align="right">28.27</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.51</td>
    <td align="right">41.13</td>
    <td align="right">21.94</td>
    <td align="right">28.03</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.84</td>
    <td align="right">64.56</td>
    <td align="right">64.67</td>
    <td align="right">64.67</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.27</td>
    <td align="right">34.79</td>
    <td align="right">14.30</td>
    <td align="right">17.67</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.76</td>
    <td align="right">44.22</td>
    <td align="right">37.69</td>
    <td align="right">39.08</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">16.22</td>
    <td align="right">16.24</td>
    <td align="right">16.20</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.58</td>
    <td align="right">18.05</td>
    <td align="right">17.68</td>
    <td align="right">18.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.89</td>
    <td align="right">67.36</td>
    <td align="right">40.65</td>
    <td align="right">45.30</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.37</td>
    <td align="right">18.41</td>
    <td align="right">18.29</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.05</td>
    <td align="right">19.25</td>
    <td align="right">19.11</td>
    <td align="right">19.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.00</td>
    <td align="right">81.84</td>
    <td align="right">38.93</td>
    <td align="right">45.24</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.43</td>
    <td align="right">20.52</td>
    <td align="right">20.47</td>
    <td align="right">20.48</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.92</td>
    <td align="right">21.34</td>
    <td align="right">20.99</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.84</td>
    <td align="right">104.25</td>
    <td align="right">41.02</td>
    <td align="right">48.54</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.65</td>
    <td align="right">22.17</td>
    <td align="right">22.20</td>
    <td align="right">22.19</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.02</td>
    <td align="right">22.34</td>
    <td align="right">22.89</td>
    <td align="right">21.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.90</td>
    <td align="right">23.82</td>
    <td align="right">23.83</td>
    <td align="right">23.71</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.63</td>
    <td align="right">26.54</td>
    <td align="right">26.53</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.94</td>
    <td align="right">15.55</td>
    <td align="right">15.62</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.39</td>
    <td align="right">29.99</td>
    <td align="right">30.06</td>
    <td align="right">29.95</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.56</td>
    <td align="right">34.57</td>
    <td align="right">34.57</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.96</td>
    <td align="right">17.77</td>
    <td align="right">17.77</td>
    <td align="right">17.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.48</td>
    <td align="right">36.92</td>
    <td align="right">37.01</td>
    <td align="right">37.07</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.59</td>
    <td align="right">49.16</td>
    <td align="right">49.05</td>
    <td align="right">49.06</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.10</td>
    <td align="right">20.83</td>
    <td align="right">20.83</td>
    <td align="right">20.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.15</td>
    <td align="right">41.52</td>
    <td align="right">41.65</td>
    <td align="right">41.65</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.52</td>
    <td align="right">58.51</td>
    <td align="right">58.54</td>
    <td align="right">58.52</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.86</td>
    <td align="right">26.15</td>
    <td align="right">26.07</td>
    <td align="right">26.04</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.40</td>
    <td align="right">16.80</td>
    <td align="right">16.81</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.92</td>
    <td align="right">23.80</td>
    <td align="right">23.76</td>
    <td align="right">23.65</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.52</td>
    <td align="right">26.52</td>
    <td align="right">26.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">18.98</td>
    <td align="right">21.14</td>
    <td align="right">21.06</td>
    <td align="right">21.19</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.67</td>
    <td align="right">30.05</td>
    <td align="right">30.08</td>
    <td align="right">30.13</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">34.59</td>
    <td align="right">34.60</td>
    <td align="right">34.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.44</td>
    <td align="right">25.10</td>
    <td align="right">25.08</td>
    <td align="right">25.17</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.55</td>
    <td align="right">37.32</td>
    <td align="right">36.92</td>
    <td align="right">37.14</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.64</td>
    <td align="right">49.11</td>
    <td align="right">49.00</td>
    <td align="right">49.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.70</td>
    <td align="right">33.09</td>
    <td align="right">33.09</td>
    <td align="right">33.09</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">41.76</td>
    <td align="right">41.71</td>
    <td align="right">41.55</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.38</td>
    <td align="right">58.51</td>
    <td align="right">58.58</td>
    <td align="right">58.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.31</td>
    <td align="right">24.51</td>
    <td align="right">27.76</td>
    <td align="right">29.63</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.66</td>
    <td align="right">31.49</td>
    <td align="right">35.58</td>
    <td align="right">35.63</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.31</td>
    <td align="right">34.49</td>
    <td align="right">34.69</td>
    <td align="right">34.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.37</td>
    <td align="right">37.02</td>
    <td align="right">29.64</td>
    <td align="right">32.14</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.33</td>
    <td align="right">40.90</td>
    <td align="right">34.54</td>
    <td align="right">37.24</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.62</td>
    <td align="right">44.84</td>
    <td align="right">44.81</td>
    <td align="right">44.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.11</td>
    <td align="right">43.84</td>
    <td align="right">27.92</td>
    <td align="right">32.66</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.53</td>
    <td align="right">50.35</td>
    <td align="right">36.10</td>
    <td align="right">39.51</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.11</td>
    <td align="right">47.03</td>
    <td align="right">47.06</td>
    <td align="right">47.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.27</td>
    <td align="right">49.12</td>
    <td align="right">29.41</td>
    <td align="right">33.86</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.34</td>
    <td align="right">52.60</td>
    <td align="right">36.00</td>
    <td align="right">39.70</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.97</td>
    <td align="right">65.41</td>
    <td align="right">65.10</td>
    <td align="right">65.42</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">109.37</td>
    <td align="right">130.08</td>
    <td align="right">27.68</td>
    <td align="right">41.69</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">43.36</td>
    <td align="right">59.56</td>
    <td align="right">46.30</td>
    <td align="right">48.28</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.86</td>
    <td align="right">19.08</td>
    <td align="right">18.86</td>
    <td align="right">18.74</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.36</td>
    <td align="right">20.61</td>
    <td align="right">20.60</td>
    <td align="right">20.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">108.33</td>
    <td align="right">140.33</td>
    <td align="right">62.76</td>
    <td align="right">72.49</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.60</td>
    <td align="right">29.56</td>
    <td align="right">29.39</td>
    <td align="right">29.67</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.51</td>
    <td align="right">33.44</td>
    <td align="right">33.32</td>
    <td align="right">33.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">195.97</td>
    <td align="right">257.37</td>
    <td align="right">80.03</td>
    <td align="right">99.71</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.09</td>
    <td align="right">47.50</td>
    <td align="right">47.53</td>
    <td align="right">47.48</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.64</td>
    <td align="right">51.63</td>
    <td align="right">51.41</td>
    <td align="right">51.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">301.96</td>
    <td align="right">411.37</td>
    <td align="right">100.59</td>
    <td align="right">133.49</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.92</td>
    <td align="right">65.55</td>
    <td align="right">65.72</td>
    <td align="right">65.52</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">64.32</td>
    <td align="right">66.69</td>
    <td align="right">66.59</td>
    <td align="right">66.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.02</td>
    <td align="right">28.13</td>
    <td align="right">28.18</td>
    <td align="right">28.18</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.92</td>
    <td align="right">33.45</td>
    <td align="right">33.41</td>
    <td align="right">33.36</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.94</td>
    <td align="right">20.62</td>
    <td align="right">19.98</td>
    <td align="right">20.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.10</td>
    <td align="right">45.16</td>
    <td align="right">45.10</td>
    <td align="right">45.11</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">56.03</td>
    <td align="right">49.93</td>
    <td align="right">49.96</td>
    <td align="right">49.73</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.74</td>
    <td align="right">26.91</td>
    <td align="right">26.83</td>
    <td align="right">26.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.89</td>
    <td align="right">73.06</td>
    <td align="right">73.22</td>
    <td align="right">73.10</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.67</td>
    <td align="right">84.32</td>
    <td align="right">84.32</td>
    <td align="right">84.25</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.65</td>
    <td align="right">45.93</td>
    <td align="right">45.92</td>
    <td align="right">45.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.35</td>
    <td align="right">95.04</td>
    <td align="right">94.87</td>
    <td align="right">94.78</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.88</td>
    <td align="right">111.47</td>
    <td align="right">111.52</td>
    <td align="right">111.52</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">71.12</td>
    <td align="right">76.68</td>
    <td align="right">76.57</td>
    <td align="right">76.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.63</td>
    <td align="right">18.99</td>
    <td align="right">19.65</td>
    <td align="right">19.10</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.12</td>
    <td align="right">28.28</td>
    <td align="right">28.29</td>
    <td align="right">28.30</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.64</td>
    <td align="right">30.03</td>
    <td align="right">30.05</td>
    <td align="right">30.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">31.55</td>
    <td align="right">33.85</td>
    <td align="right">33.88</td>
    <td align="right">33.87</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.27</td>
    <td align="right">45.74</td>
    <td align="right">45.57</td>
    <td align="right">45.53</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.05</td>
    <td align="right">51.74</td>
    <td align="right">51.65</td>
    <td align="right">51.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">49.34</td>
    <td align="right">56.59</td>
    <td align="right">56.56</td>
    <td align="right">57.63</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.32</td>
    <td align="right">72.33</td>
    <td align="right">72.64</td>
    <td align="right">72.52</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">104.45</td>
    <td align="right">84.98</td>
    <td align="right">84.96</td>
    <td align="right">84.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">83.16</td>
    <td align="right">84.33</td>
    <td align="right">84.67</td>
    <td align="right">84.12</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.87</td>
    <td align="right">94.84</td>
    <td align="right">94.99</td>
    <td align="right">94.70</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.57</td>
    <td align="right">110.35</td>
    <td align="right">110.38</td>
    <td align="right">110.50</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.21</td>
    <td align="right">28.62</td>
    <td align="right">30.45</td>
    <td align="right">33.33</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">37.41</td>
    <td align="right">38.26</td>
    <td align="right">40.39</td>
    <td align="right">41.88</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">37.72</td>
    <td align="right">42.30</td>
    <td align="right">42.17</td>
    <td align="right">42.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.68</td>
    <td align="right">51.75</td>
    <td align="right">39.11</td>
    <td align="right">42.60</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">59.11</td>
    <td align="right">59.51</td>
    <td align="right">46.24</td>
    <td align="right">49.88</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.31</td>
    <td align="right">65.78</td>
    <td align="right">65.85</td>
    <td align="right">65.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.60</td>
    <td align="right">72.20</td>
    <td align="right">47.22</td>
    <td align="right">53.57</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">87.21</td>
    <td align="right">88.52</td>
    <td align="right">60.84</td>
    <td align="right">66.99</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">89.34</td>
    <td align="right">95.61</td>
    <td align="right">95.55</td>
    <td align="right">95.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.88</td>
    <td align="right">90.33</td>
    <td align="right">57.14</td>
    <td align="right">64.74</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">106.03</td>
    <td align="right">106.08</td>
    <td align="right">69.10</td>
    <td align="right">75.68</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">136.91</td>
    <td align="right">144.90</td>
    <td align="right">144.31</td>
    <td align="right">147.58</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.18</td>
    <td align="right">14.25</td>
    <td align="right">8.56</td>
    <td align="right">11.53</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.55</td>
    <td align="right">28.42</td>
    <td align="right">29.24</td>
    <td align="right">30.09</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">14.00</td>
    <td align="right">13.92</td>
    <td align="right">13.92</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.83</td>
    <td align="right">18.03</td>
    <td align="right">18.00</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.62</td>
    <td align="right">42.66</td>
    <td align="right">31.40</td>
    <td align="right">33.81</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.00</td>
    <td align="right">18.42</td>
    <td align="right">18.41</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.19</td>
    <td align="right">20.69</td>
    <td align="right">20.69</td>
    <td align="right">20.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.61</td>
    <td align="right">66.42</td>
    <td align="right">32.23</td>
    <td align="right">37.41</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.72</td>
    <td align="right">21.35</td>
    <td align="right">21.33</td>
    <td align="right">21.34</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.09</td>
    <td align="right">22.90</td>
    <td align="right">22.77</td>
    <td align="right">22.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.73</td>
    <td align="right">81.05</td>
    <td align="right">33.09</td>
    <td align="right">40.07</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.22</td>
    <td align="right">23.32</td>
    <td align="right">23.24</td>
    <td align="right">23.24</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.03</td>
    <td align="right">25.67</td>
    <td align="right">25.68</td>
    <td align="right">25.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">18.31</td>
    <td align="right">18.31</td>
    <td align="right">18.44</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.10</td>
    <td align="right">18.85</td>
    <td align="right">18.85</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.95</td>
    <td align="right">8.70</td>
    <td align="right">8.70</td>
    <td align="right">8.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.55</td>
    <td align="right">26.49</td>
    <td align="right">26.50</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.57</td>
    <td align="right">26.90</td>
    <td align="right">26.92</td>
    <td align="right">26.91</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.92</td>
    <td align="right">13.74</td>
    <td align="right">13.72</td>
    <td align="right">13.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.15</td>
    <td align="right">35.32</td>
    <td align="right">35.29</td>
    <td align="right">35.29</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.57</td>
    <td align="right">34.16</td>
    <td align="right">34.18</td>
    <td align="right">34.32</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.83</td>
    <td align="right">17.82</td>
    <td align="right">17.81</td>
    <td align="right">17.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.54</td>
    <td align="right">38.28</td>
    <td align="right">38.26</td>
    <td align="right">38.29</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.47</td>
    <td align="right">41.20</td>
    <td align="right">41.10</td>
    <td align="right">41.08</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.07</td>
    <td align="right">19.70</td>
    <td align="right">19.70</td>
    <td align="right">19.76</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.66</td>
    <td align="right">8.48</td>
    <td align="right">8.51</td>
    <td align="right">8.93</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">18.43</td>
    <td align="right">18.44</td>
    <td align="right">18.32</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.05</td>
    <td align="right">18.83</td>
    <td align="right">18.84</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.83</td>
    <td align="right">14.10</td>
    <td align="right">14.07</td>
    <td align="right">14.08</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.65</td>
    <td align="right">26.56</td>
    <td align="right">26.53</td>
    <td align="right">26.55</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.61</td>
    <td align="right">26.95</td>
    <td align="right">26.94</td>
    <td align="right">26.93</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">17.22</td>
    <td align="right">17.24</td>
    <td align="right">17.20</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.16</td>
    <td align="right">35.32</td>
    <td align="right">35.31</td>
    <td align="right">35.30</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">34.15</td>
    <td align="right">34.15</td>
    <td align="right">34.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">20.19</td>
    <td align="right">20.00</td>
    <td align="right">20.01</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">38.26</td>
    <td align="right">38.32</td>
    <td align="right">38.31</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.37</td>
    <td align="right">41.19</td>
    <td align="right">41.12</td>
    <td align="right">41.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.29</td>
    <td align="right">20.97</td>
    <td align="right">24.61</td>
    <td align="right">26.51</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.52</td>
    <td align="right">41.94</td>
    <td align="right">41.70</td>
    <td align="right">41.98</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.84</td>
    <td align="right">26.96</td>
    <td align="right">27.15</td>
    <td align="right">27.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.00</td>
    <td align="right">30.00</td>
    <td align="right">24.23</td>
    <td align="right">27.37</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.88</td>
    <td align="right">46.25</td>
    <td align="right">39.42</td>
    <td align="right">41.86</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.61</td>
    <td align="right">36.78</td>
    <td align="right">36.83</td>
    <td align="right">36.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.15</td>
    <td align="right">35.79</td>
    <td align="right">24.47</td>
    <td align="right">28.62</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.31</td>
    <td align="right">54.02</td>
    <td align="right">40.16</td>
    <td align="right">42.89</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.47</td>
    <td align="right">38.84</td>
    <td align="right">38.78</td>
    <td align="right">38.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.75</td>
    <td align="right">46.74</td>
    <td align="right">29.68</td>
    <td align="right">33.78</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.97</td>
    <td align="right">58.30</td>
    <td align="right">45.22</td>
    <td align="right">46.87</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.19</td>
    <td align="right">50.85</td>
    <td align="right">50.50</td>
    <td align="right">50.66</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">126.47</td>
    <td align="right">63.10</td>
    <td align="right">23.35</td>
    <td align="right">33.38</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">27.89</td>
    <td align="right">35.96</td>
    <td align="right">34.62</td>
    <td align="right">35.97</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">17.10</td>
    <td align="right">18.61</td>
    <td align="right">18.54</td>
    <td align="right">18.57</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.50</td>
    <td align="right">20.40</td>
    <td align="right">20.50</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">74.74</td>
    <td align="right">91.98</td>
    <td align="right">45.67</td>
    <td align="right">51.76</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.95</td>
    <td align="right">28.42</td>
    <td align="right">28.59</td>
    <td align="right">28.54</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.19</td>
    <td align="right">30.19</td>
    <td align="right">30.47</td>
    <td align="right">30.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">149.75</td>
    <td align="right">210.55</td>
    <td align="right">68.22</td>
    <td align="right">84.83</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.98</td>
    <td align="right">49.57</td>
    <td align="right">49.49</td>
    <td align="right">49.57</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.63</td>
    <td align="right">51.44</td>
    <td align="right">51.17</td>
    <td align="right">51.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">251.81</td>
    <td align="right">336.18</td>
    <td align="right">84.86</td>
    <td align="right">108.88</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">66.06</td>
    <td align="right">65.43</td>
    <td align="right">65.56</td>
    <td align="right">65.74</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">69.88</td>
    <td align="right">69.63</td>
    <td align="right">69.70</td>
    <td align="right">69.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.02</td>
    <td align="right">21.50</td>
    <td align="right">21.53</td>
    <td align="right">21.69</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.34</td>
    <td align="right">22.91</td>
    <td align="right">22.85</td>
    <td align="right">22.86</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">8.95</td>
    <td align="right">9.69</td>
    <td align="right">9.74</td>
    <td align="right">9.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.92</td>
    <td align="right">42.40</td>
    <td align="right">42.09</td>
    <td align="right">42.05</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.09</td>
    <td align="right">45.34</td>
    <td align="right">45.42</td>
    <td align="right">45.58</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.40</td>
    <td align="right">23.16</td>
    <td align="right">24.09</td>
    <td align="right">23.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.24</td>
    <td align="right">70.37</td>
    <td align="right">70.17</td>
    <td align="right">70.24</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">72.18</td>
    <td align="right">68.60</td>
    <td align="right">68.67</td>
    <td align="right">68.74</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">39.24</td>
    <td align="right">41.77</td>
    <td align="right">41.87</td>
    <td align="right">41.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.74</td>
    <td align="right">88.80</td>
    <td align="right">88.82</td>
    <td align="right">88.85</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.52</td>
    <td align="right">93.65</td>
    <td align="right">93.83</td>
    <td align="right">94.85</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">54.62</td>
    <td align="right">53.56</td>
    <td align="right">53.74</td>
    <td align="right">53.39</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.29</td>
    <td align="right">10.70</td>
    <td align="right">10.42</td>
    <td align="right">10.31</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.07</td>
    <td align="right">21.55</td>
    <td align="right">21.54</td>
    <td align="right">21.60</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.32</td>
    <td align="right">23.00</td>
    <td align="right">22.89</td>
    <td align="right">22.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">22.35</td>
    <td align="right">25.23</td>
    <td align="right">24.60</td>
    <td align="right">24.65</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.64</td>
    <td align="right">41.92</td>
    <td align="right">41.82</td>
    <td align="right">41.76</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.95</td>
    <td align="right">46.20</td>
    <td align="right">46.32</td>
    <td align="right">46.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">39.47</td>
    <td align="right">41.84</td>
    <td align="right">41.97</td>
    <td align="right">41.75</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.73</td>
    <td align="right">70.92</td>
    <td align="right">70.85</td>
    <td align="right">70.70</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">72.82</td>
    <td align="right">70.35</td>
    <td align="right">70.35</td>
    <td align="right">70.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">54.61</td>
    <td align="right">54.74</td>
    <td align="right">54.73</td>
    <td align="right">54.66</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.62</td>
    <td align="right">90.43</td>
    <td align="right">90.42</td>
    <td align="right">90.40</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">98.57</td>
    <td align="right">95.93</td>
    <td align="right">96.25</td>
    <td align="right">97.00</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">20.01</td>
    <td align="right">23.10</td>
    <td align="right">26.07</td>
    <td align="right">28.60</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.42</td>
    <td align="right">43.03</td>
    <td align="right">42.85</td>
    <td align="right">43.01</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.67</td>
    <td align="right">33.41</td>
    <td align="right">33.59</td>
    <td align="right">34.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.91</td>
    <td align="right">45.33</td>
    <td align="right">32.64</td>
    <td align="right">37.66</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">66.98</td>
    <td align="right">59.97</td>
    <td align="right">50.38</td>
    <td align="right">53.67</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">59.88</td>
    <td align="right">59.77</td>
    <td align="right">59.95</td>
    <td align="right">59.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">63.46</td>
    <td align="right">66.05</td>
    <td align="right">41.81</td>
    <td align="right">48.76</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.00</td>
    <td align="right">88.87</td>
    <td align="right">64.55</td>
    <td align="right">69.84</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.41</td>
    <td align="right">81.60</td>
    <td align="right">81.58</td>
    <td align="right">81.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.84</td>
    <td align="right">89.12</td>
    <td align="right">57.91</td>
    <td align="right">65.32</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">111.24</td>
    <td align="right">107.43</td>
    <td align="right">81.00</td>
    <td align="right">84.78</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">127.97</td>
    <td align="right">120.24</td>
    <td align="right">119.77</td>
    <td align="right">120.18</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.77</td>
    <td align="right">6.63</td>
    <td align="right">5.67</td>
    <td align="right">7.68</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.26</td>
    <td align="right">59.60</td>
    <td align="right">39.71</td>
    <td align="right">42.97</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.88</td>
    <td align="right">20.60</td>
    <td align="right">23.32</td>
    <td align="right">24.04</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.78</td>
    <td align="right">24.92</td>
    <td align="right">26.56</td>
    <td align="right">27.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.13</td>
    <td align="right">86.80</td>
    <td align="right">42.44</td>
    <td align="right">46.28</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.31</td>
    <td align="right">22.32</td>
    <td align="right">24.39</td>
    <td align="right">25.23</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.58</td>
    <td align="right">27.76</td>
    <td align="right">28.44</td>
    <td align="right">29.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">131.07</td>
    <td align="right">104.72</td>
    <td align="right">40.31</td>
    <td align="right">46.51</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.25</td>
    <td align="right">25.72</td>
    <td align="right">25.99</td>
    <td align="right">26.87</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.86</td>
    <td align="right">29.97</td>
    <td align="right">29.64</td>
    <td align="right">30.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">157.86</td>
    <td align="right">134.36</td>
    <td align="right">41.65</td>
    <td align="right">50.65</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">39.13</td>
    <td align="right">37.09</td>
    <td align="right">37.92</td>
    <td align="right">39.01</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.06</td>
    <td align="right">31.81</td>
    <td align="right">31.76</td>
    <td align="right">32.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.19</td>
    <td align="right">41.02</td>
    <td align="right">41.18</td>
    <td align="right">40.87</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.42</td>
    <td align="right">41.90</td>
    <td align="right">41.15</td>
    <td align="right">41.32</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.55</td>
    <td align="right">28.29</td>
    <td align="right">28.00</td>
    <td align="right">27.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.58</td>
    <td align="right">55.73</td>
    <td align="right">55.50</td>
    <td align="right">55.29</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">31.77</td>
    <td align="right">55.83</td>
    <td align="right">55.56</td>
    <td align="right">55.71</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.81</td>
    <td align="right">37.05</td>
    <td align="right">27.45</td>
    <td align="right">29.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.90</td>
    <td align="right">77.38</td>
    <td align="right">76.98</td>
    <td align="right">77.11</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.81</td>
    <td align="right">77.03</td>
    <td align="right">77.02</td>
    <td align="right">77.01</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.58</td>
    <td align="right">53.89</td>
    <td align="right">37.07</td>
    <td align="right">38.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.78</td>
    <td align="right">84.11</td>
    <td align="right">84.10</td>
    <td align="right">83.95</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.19</td>
    <td align="right">90.64</td>
    <td align="right">89.31</td>
    <td align="right">89.29</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.08</td>
    <td align="right">53.93</td>
    <td align="right">37.37</td>
    <td align="right">39.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.84</td>
    <td align="right">28.24</td>
    <td align="right">28.21</td>
    <td align="right">27.86</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.75</td>
    <td align="right">30.44</td>
    <td align="right">30.22</td>
    <td align="right">30.23</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.31</td>
    <td align="right">30.62</td>
    <td align="right">30.37</td>
    <td align="right">30.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.05</td>
    <td align="right">43.78</td>
    <td align="right">34.32</td>
    <td align="right">35.88</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.95</td>
    <td align="right">38.59</td>
    <td align="right">28.99</td>
    <td align="right">30.66</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.74</td>
    <td align="right">46.57</td>
    <td align="right">36.98</td>
    <td align="right">38.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.65</td>
    <td align="right">53.55</td>
    <td align="right">36.68</td>
    <td align="right">38.50</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">32.87</td>
    <td align="right">57.50</td>
    <td align="right">39.75</td>
    <td align="right">41.91</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.16</td>
    <td align="right">57.34</td>
    <td align="right">39.68</td>
    <td align="right">41.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.21</td>
    <td align="right">53.57</td>
    <td align="right">36.84</td>
    <td align="right">38.91</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.63</td>
    <td align="right">59.38</td>
    <td align="right">40.12</td>
    <td align="right">42.37</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.97</td>
    <td align="right">58.97</td>
    <td align="right">39.77</td>
    <td align="right">42.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">26.95</td>
    <td align="right">44.27</td>
    <td align="right">33.55</td>
    <td align="right">35.93</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.48</td>
    <td align="right">55.32</td>
    <td align="right">37.67</td>
    <td align="right">38.49</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.17</td>
    <td align="right">60.42</td>
    <td align="right">60.47</td>
    <td align="right">60.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.54</td>
    <td align="right">62.42</td>
    <td align="right">33.51</td>
    <td align="right">41.63</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.04</td>
    <td align="right">63.07</td>
    <td align="right">35.25</td>
    <td align="right">39.01</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.43</td>
    <td align="right">78.46</td>
    <td align="right">78.36</td>
    <td align="right">78.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.85</td>
    <td align="right">73.91</td>
    <td align="right">32.88</td>
    <td align="right">38.00</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">54.32</td>
    <td align="right">97.47</td>
    <td align="right">57.97</td>
    <td align="right">61.57</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.54</td>
    <td align="right">84.83</td>
    <td align="right">85.31</td>
    <td align="right">84.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">52.14</td>
    <td align="right">101.32</td>
    <td align="right">34.65</td>
    <td align="right">42.44</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.28</td>
    <td align="right">101.68</td>
    <td align="right">36.87</td>
    <td align="right">44.47</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.03</td>
    <td align="right">117.99</td>
    <td align="right">118.01</td>
    <td align="right">117.83</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">66.07</td>
    <td align="right">33.51</td>
    <td align="right">18.92</td>
    <td align="right">25.56</td>
  </tr>
</table>
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">101.62</td>
    <td align="right">119.74</td>
    <td align="right">62.91</td>
    <td align="right">69.46</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">43.12</td>
    <td align="right">40.10</td>
    <td align="right">43.52</td>
    <td align="right">44.54</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">58.57</td>
    <td align="right">65.18</td>
    <td align="right">65.66</td>
    <td align="right">66.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">192.04</td>
    <td align="right">176.03</td>
    <td align="right">65.14</td>
    <td align="right">76.25</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">28.17</td>
    <td align="right">25.27</td>
    <td align="right">27.26</td>
    <td align="right">28.82</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">33.98</td>
    <td align="right">41.52</td>
    <td align="right">41.89</td>
    <td align="right">43.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">272.07</td>
    <td align="right">228.20</td>
    <td align="right">65.83</td>
    <td align="right">83.38</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">38.00</td>
    <td align="right">37.95</td>
    <td align="right">38.82</td>
    <td align="right">39.97</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">49.04</td>
    <td align="right">49.98</td>
    <td align="right">49.62</td>
    <td align="right">50.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">442.26</td>
    <td align="right">354.73</td>
    <td align="right">79.57</td>
    <td align="right">107.64</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.22</td>
    <td align="right">44.44</td>
    <td align="right">45.64</td>
    <td align="right">46.75</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.14</td>
    <td align="right">62.70</td>
    <td align="right">63.13</td>
    <td align="right">64.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.70</td>
    <td align="right">41.30</td>
    <td align="right">41.61</td>
    <td align="right">41.32</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">32.06</td>
    <td align="right">42.22</td>
    <td align="right">41.46</td>
    <td align="right">41.57</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">19.25</td>
    <td align="right">30.45</td>
    <td align="right">30.36</td>
    <td align="right">30.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.63</td>
    <td align="right">57.76</td>
    <td align="right">57.34</td>
    <td align="right">57.13</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.44</td>
    <td align="right">58.39</td>
    <td align="right">58.46</td>
    <td align="right">58.46</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.90</td>
    <td align="right">40.70</td>
    <td align="right">31.26</td>
    <td align="right">33.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.54</td>
    <td align="right">90.36</td>
    <td align="right">90.34</td>
    <td align="right">90.24</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">62.97</td>
    <td align="right">92.40</td>
    <td align="right">92.55</td>
    <td align="right">92.36</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.29</td>
    <td align="right">76.71</td>
    <td align="right">59.51</td>
    <td align="right">61.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.27</td>
    <td align="right">107.36</td>
    <td align="right">107.32</td>
    <td align="right">107.33</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.46</td>
    <td align="right">119.50</td>
    <td align="right">118.50</td>
    <td align="right">118.46</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">65.40</td>
    <td align="right">96.11</td>
    <td align="right">80.24</td>
    <td align="right">81.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.33</td>
    <td align="right">30.06</td>
    <td align="right">29.99</td>
    <td align="right">29.92</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.18</td>
    <td align="right">32.16</td>
    <td align="right">31.99</td>
    <td align="right">32.02</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.82</td>
    <td align="right">31.99</td>
    <td align="right">31.95</td>
    <td align="right">31.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.45</td>
    <td align="right">48.26</td>
    <td align="right">38.83</td>
    <td align="right">40.58</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">23.82</td>
    <td align="right">49.87</td>
    <td align="right">40.04</td>
    <td align="right">41.85</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">24.64</td>
    <td align="right">50.97</td>
    <td align="right">41.72</td>
    <td align="right">43.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.97</td>
    <td align="right">78.36</td>
    <td align="right">61.14</td>
    <td align="right">63.10</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.02</td>
    <td align="right">80.92</td>
    <td align="right">63.06</td>
    <td align="right">65.61</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">52.05</td>
    <td align="right">80.27</td>
    <td align="right">62.54</td>
    <td align="right">64.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.97</td>
    <td align="right">92.64</td>
    <td align="right">74.76</td>
    <td align="right">76.81</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.55</td>
    <td align="right">97.88</td>
    <td align="right">77.86</td>
    <td align="right">80.35</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.59</td>
    <td align="right">97.86</td>
    <td align="right">78.09</td>
    <td align="right">80.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">33.75</td>
    <td align="right">44.64</td>
    <td align="right">35.10</td>
    <td align="right">37.39</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.45</td>
    <td align="right">55.73</td>
    <td align="right">39.02</td>
    <td align="right">40.70</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">43.34</td>
    <td align="right">60.70</td>
    <td align="right">60.72</td>
    <td align="right">60.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">43.54</td>
    <td align="right">65.57</td>
    <td align="right">37.65</td>
    <td align="right">41.54</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">48.22</td>
    <td align="right">65.57</td>
    <td align="right">38.73</td>
    <td align="right">42.75</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">54.46</td>
    <td align="right">94.90</td>
    <td align="right">94.93</td>
    <td align="right">94.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">60.21</td>
    <td align="right">87.66</td>
    <td align="right">51.41</td>
    <td align="right">56.40</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.30</td>
    <td align="right">99.36</td>
    <td align="right">59.55</td>
    <td align="right">65.20</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.04</td>
    <td align="right">102.97</td>
    <td align="right">103.00</td>
    <td align="right">103.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">80.42</td>
    <td align="right">123.03</td>
    <td align="right">63.18</td>
    <td align="right">70.03</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.10</td>
    <td align="right">133.66</td>
    <td align="right">74.20</td>
    <td align="right">80.90</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">107.84</td>
    <td align="right">144.68</td>
    <td align="right">144.86</td>
    <td align="right">144.73</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
