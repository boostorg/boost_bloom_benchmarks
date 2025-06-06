# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.29</td>
    <td align="right">4.56</td>
    <td align="right">3.54</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.31</td>
    <td align="right">10.79</td>
    <td align="right">16.76</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.02</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.93</td>
    <td align="right">5.12</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.15</td>
    <td align="right">15.72</td>
    <td align="right">17.78</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.87</td>
    <td align="right">4.98</td>
    <td align="right">5.03</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.48</td>
    <td align="right">5.55</td>
    <td align="right">5.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.32</td>
    <td align="right">19.03</td>
    <td align="right">16.68</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.47</td>
    <td align="right">5.36</td>
    <td align="right">5.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.32</td>
    <td align="right">6.37</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.90</td>
    <td align="right">23.43</td>
    <td align="right">16.86</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.23</td>
    <td align="right">5.95</td>
    <td align="right">5.94</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.76</td>
    <td align="right">6.66</td>
    <td align="right">6.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.15</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.32</td>
    <td align="right">6.64</td>
    <td align="right">6.63</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.99</td>
    <td align="right">3.35</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.56</td>
    <td align="right">7.77</td>
    <td align="right">7.80</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.15</td>
    <td align="right">9.76</td>
    <td align="right">9.74</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.51</td>
    <td align="right">3.16</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.44</td>
    <td align="right">13.94</td>
    <td align="right">14.28</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">17.06</td>
    <td align="right">14.22</td>
    <td align="right">14.23</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.81</td>
    <td align="right">5.84</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.21</td>
    <td align="right">15.62</td>
    <td align="right">15.67</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.32</td>
    <td align="right">17.56</td>
    <td align="right">17.55</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.84</td>
    <td align="right">5.87</td>
    <td align="right">3.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.96</td>
    <td align="right">3.26</td>
    <td align="right">3.26</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.43</td>
    <td align="right">5.12</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.60</td>
    <td align="right">5.02</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.09</td>
    <td align="right">3.31</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.23</td>
    <td align="right">4.46</td>
    <td align="right">4.48</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.50</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.42</td>
    <td align="right">5.56</td>
    <td align="right">3.80</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.09</td>
    <td align="right">7.75</td>
    <td align="right">5.94</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.94</td>
    <td align="right">7.62</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.52</td>
    <td align="right">5.60</td>
    <td align="right">3.83</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">8.07</td>
    <td align="right">9.14</td>
    <td align="right">5.98</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.39</td>
    <td align="right">9.08</td>
    <td align="right">5.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.88</td>
    <td align="right">6.97</td>
    <td align="right">13.57</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.47</td>
    <td align="right">9.00</td>
    <td align="right">17.46</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.69</td>
    <td align="right">11.63</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.41</td>
    <td align="right">8.42</td>
    <td align="right">12.44</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.26</td>
    <td align="right">9.58</td>
    <td align="right">14.35</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.59</td>
    <td align="right">14.94</td>
    <td align="right">14.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.00</td>
    <td align="right">10.40</td>
    <td align="right">12.12</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.50</td>
    <td align="right">12.65</td>
    <td align="right">15.31</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.69</td>
    <td align="right">17.39</td>
    <td align="right">18.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.54</td>
    <td align="right">12.77</td>
    <td align="right">13.20</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.77</td>
    <td align="right">14.19</td>
    <td align="right">14.91</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.95</td>
    <td align="right">22.42</td>
    <td align="right">22.44</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.12</td>
    <td align="right">17.66</td>
    <td align="right">6.64</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.88</td>
    <td align="right">12.98</td>
    <td align="right">17.80</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.76</td>
    <td align="right">5.08</td>
    <td align="right">5.07</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.74</td>
    <td align="right">5.96</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">20.06</td>
    <td align="right">18.75</td>
    <td align="right">18.30</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.55</td>
    <td align="right">5.47</td>
    <td align="right">5.50</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.08</td>
    <td align="right">6.60</td>
    <td align="right">6.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">32.53</td>
    <td align="right">30.10</td>
    <td align="right">18.36</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.15</td>
    <td align="right">6.65</td>
    <td align="right">6.87</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.91</td>
    <td align="right">7.69</td>
    <td align="right">7.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">52.39</td>
    <td align="right">52.73</td>
    <td align="right">19.62</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.15</td>
    <td align="right">11.58</td>
    <td align="right">12.01</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.46</td>
    <td align="right">10.44</td>
    <td align="right">10.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.99</td>
    <td align="right">6.80</td>
    <td align="right">6.80</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.21</td>
    <td align="right">7.80</td>
    <td align="right">7.89</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.54</td>
    <td align="right">4.04</td>
    <td align="right">4.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.88</td>
    <td align="right">22.84</td>
    <td align="right">12.21</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.61</td>
    <td align="right">14.64</td>
    <td align="right">13.86</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.72</td>
    <td align="right">4.36</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.45</td>
    <td align="right">16.23</td>
    <td align="right">16.58</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">21.31</td>
    <td align="right">15.51</td>
    <td align="right">15.68</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.68</td>
    <td align="right">7.77</td>
    <td align="right">6.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.61</td>
    <td align="right">18.58</td>
    <td align="right">17.53</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">23.43</td>
    <td align="right">23.22</td>
    <td align="right">23.59</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.06</td>
    <td align="right">11.07</td>
    <td align="right">7.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.51</td>
    <td align="right">3.96</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.17</td>
    <td align="right">6.02</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.34</td>
    <td align="right">5.94</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.53</td>
    <td align="right">3.92</td>
    <td align="right">3.86</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.63</td>
    <td align="right">5.00</td>
    <td align="right">6.48</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">5.02</td>
    <td align="right">5.73</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.86</td>
    <td align="right">7.44</td>
    <td align="right">5.21</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">9.00</td>
    <td align="right">10.38</td>
    <td align="right">8.09</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.62</td>
    <td align="right">10.11</td>
    <td align="right">8.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.30</td>
    <td align="right">10.16</td>
    <td align="right">7.02</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">12.74</td>
    <td align="right">14.18</td>
    <td align="right">9.56</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.30</td>
    <td align="right">15.30</td>
    <td align="right">10.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.13</td>
    <td align="right">8.25</td>
    <td align="right">14.16</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.74</td>
    <td align="right">10.32</td>
    <td align="right">18.26</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.41</td>
    <td align="right">14.14</td>
    <td align="right">14.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.27</td>
    <td align="right">9.14</td>
    <td align="right">12.73</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.34</td>
    <td align="right">10.35</td>
    <td align="right">14.66</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.40</td>
    <td align="right">18.16</td>
    <td align="right">18.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.05</td>
    <td align="right">12.12</td>
    <td align="right">13.38</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">19.16</td>
    <td align="right">15.93</td>
    <td align="right">16.79</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">20.64</td>
    <td align="right">20.60</td>
    <td align="right">21.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">21.18</td>
    <td align="right">18.54</td>
    <td align="right">15.79</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">30.07</td>
    <td align="right">22.85</td>
    <td align="right">17.77</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">30.52</td>
    <td align="right">30.66</td>
    <td align="right">30.06</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.03</td>
    <td align="right">4.27</td>
    <td align="right">3.59</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.38</td>
    <td align="right">8.98</td>
    <td align="right">15.46</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.38</td>
    <td align="right">4.00</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.90</td>
    <td align="right">4.71</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.28</td>
    <td align="right">13.60</td>
    <td align="right">16.64</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.89</td>
    <td align="right">4.64</td>
    <td align="right">4.78</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.57</td>
    <td align="right">5.53</td>
    <td align="right">5.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.51</td>
    <td align="right">16.83</td>
    <td align="right">15.67</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.36</td>
    <td align="right">5.10</td>
    <td align="right">5.14</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.94</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.41</td>
    <td align="right">21.16</td>
    <td align="right">16.10</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.83</td>
    <td align="right">5.71</td>
    <td align="right">5.70</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.88</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.07</td>
    <td align="right">3.61</td>
    <td align="right">3.63</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.19</td>
    <td align="right">3.53</td>
    <td align="right">3.54</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.59</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.71</td>
    <td align="right">4.10</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.72</td>
    <td align="right">4.40</td>
    <td align="right">4.41</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.16</td>
    <td align="right">2.28</td>
    <td align="right">2.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.64</td>
    <td align="right">7.19</td>
    <td align="right">7.19</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.80</td>
    <td align="right">7.05</td>
    <td align="right">7.03</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.22</td>
    <td align="right">4.44</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.05</td>
    <td align="right">7.80</td>
    <td align="right">7.83</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.39</td>
    <td align="right">8.27</td>
    <td align="right">8.13</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.26</td>
    <td align="right">4.70</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.59</td>
    <td align="right">2.32</td>
    <td align="right">2.32</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.58</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.74</td>
    <td align="right">3.91</td>
    <td align="right">3.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.67</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.89</td>
    <td align="right">3.72</td>
    <td align="right">3.72</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.83</td>
    <td align="right">4.03</td>
    <td align="right">4.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.23</td>
    <td align="right">4.28</td>
    <td align="right">2.95</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.54</td>
    <td align="right">6.09</td>
    <td align="right">4.60</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.72</td>
    <td align="right">5.93</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.30</td>
    <td align="right">4.34</td>
    <td align="right">2.94</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.84</td>
    <td align="right">7.19</td>
    <td align="right">4.70</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.99</td>
    <td align="right">7.16</td>
    <td align="right">4.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.70</td>
    <td align="right">6.10</td>
    <td align="right">12.20</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.29</td>
    <td align="right">7.97</td>
    <td align="right">16.62</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.61</td>
    <td align="right">11.12</td>
    <td align="right">11.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.41</td>
    <td align="right">8.15</td>
    <td align="right">12.04</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.03</td>
    <td align="right">9.52</td>
    <td align="right">14.09</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.77</td>
    <td align="right">15.14</td>
    <td align="right">15.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.59</td>
    <td align="right">10.13</td>
    <td align="right">12.01</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.94</td>
    <td align="right">12.58</td>
    <td align="right">14.83</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.43</td>
    <td align="right">17.04</td>
    <td align="right">17.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.79</td>
    <td align="right">12.23</td>
    <td align="right">12.64</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.80</td>
    <td align="right">13.81</td>
    <td align="right">14.67</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.91</td>
    <td align="right">22.68</td>
    <td align="right">22.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.11</td>
    <td align="right">16.86</td>
    <td align="right">9.43</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.35</td>
    <td align="right">10.99</td>
    <td align="right">16.58</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.06</td>
    <td align="right">5.14</td>
    <td align="right">4.94</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.80</td>
    <td align="right">5.52</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.86</td>
    <td align="right">17.25</td>
    <td align="right">17.52</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.55</td>
    <td align="right">5.12</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.12</td>
    <td align="right">6.09</td>
    <td align="right">6.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">21.33</td>
    <td align="right">23.49</td>
    <td align="right">16.75</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.40</td>
    <td align="right">6.14</td>
    <td align="right">6.02</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.91</td>
    <td align="right">7.04</td>
    <td align="right">7.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">40.75</td>
    <td align="right">43.17</td>
    <td align="right">20.98</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.07</td>
    <td align="right">8.20</td>
    <td align="right">8.09</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">5.29</td>
    <td align="right">5.80</td>
    <td align="right">5.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.74</td>
    <td align="right">4.34</td>
    <td align="right">4.31</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.82</td>
    <td align="right">4.37</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.21</td>
    <td align="right">4.58</td>
    <td align="right">4.58</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.40</td>
    <td align="right">5.78</td>
    <td align="right">5.43</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.47</td>
    <td align="right">2.99</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.93</td>
    <td align="right">8.81</td>
    <td align="right">8.60</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">7.29</td>
    <td align="right">10.02</td>
    <td align="right">8.86</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.04</td>
    <td align="right">5.37</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">7.96</td>
    <td align="right">10.06</td>
    <td align="right">12.89</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">9.00</td>
    <td align="right">11.72</td>
    <td align="right">11.59</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.09</td>
    <td align="right">9.03</td>
    <td align="right">5.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.12</td>
    <td align="right">2.98</td>
    <td align="right">2.98</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.32</td>
    <td align="right">4.88</td>
    <td align="right">4.89</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.46</td>
    <td align="right">4.79</td>
    <td align="right">4.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.01</td>
    <td align="right">2.85</td>
    <td align="right">2.97</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.39</td>
    <td align="right">4.44</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.38</td>
    <td align="right">4.76</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.79</td>
    <td align="right">5.32</td>
    <td align="right">3.75</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">6.85</td>
    <td align="right">7.74</td>
    <td align="right">6.48</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">7.16</td>
    <td align="right">7.55</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.65</td>
    <td align="right">9.65</td>
    <td align="right">4.91</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">9.18</td>
    <td align="right">10.05</td>
    <td align="right">7.20</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">9.96</td>
    <td align="right">10.53</td>
    <td align="right">7.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.01</td>
    <td align="right">7.19</td>
    <td align="right">12.69</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.83</td>
    <td align="right">9.35</td>
    <td align="right">17.25</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.89</td>
    <td align="right">16.31</td>
    <td align="right">16.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.51</td>
    <td align="right">9.52</td>
    <td align="right">12.59</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.52</td>
    <td align="right">10.36</td>
    <td align="right">14.40</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">22.18</td>
    <td align="right">22.22</td>
    <td align="right">22.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">13.64</td>
    <td align="right">11.66</td>
    <td align="right">12.73</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">19.32</td>
    <td align="right">14.52</td>
    <td align="right">15.50</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">25.25</td>
    <td align="right">25.36</td>
    <td align="right">25.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">19.14</td>
    <td align="right">15.81</td>
    <td align="right">13.73</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">25.65</td>
    <td align="right">18.27</td>
    <td align="right">16.89</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">33.39</td>
    <td align="right">31.82</td>
    <td align="right">30.90</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">21.21</td>
    <td align="right">2.62</td>
    <td align="right">1.97</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.35</td>
    <td align="right">6.16</td>
    <td align="right">12.15</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.39</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.63</td>
    <td align="right">1.51</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.46</td>
    <td align="right">6.72</td>
    <td align="right">11.80</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.39</td>
    <td align="right">1.54</td>
    <td align="right">1.65</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.72</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.37</td>
    <td align="right">8.32</td>
    <td align="right">11.42</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.72</td>
    <td align="right">1.75</td>
    <td align="right">1.79</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.92</td>
    <td align="right">1.77</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">18.34</td>
    <td align="right">11.79</td>
    <td align="right">12.55</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="right">2.06</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.92</td>
    <td align="right">1.70</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.44</td>
    <td align="right">1.83</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.49</td>
    <td align="right">1.88</td>
    <td align="right">1.86</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.07</td>
    <td align="right">1.79</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.40</td>
    <td align="right">2.20</td>
    <td align="right">2.19</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.03</td>
    <td align="right">2.41</td>
    <td align="right">2.45</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.67</td>
    <td align="right">1.42</td>
    <td align="right">1.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.50</td>
    <td align="right">3.22</td>
    <td align="right">3.14</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.84</td>
    <td align="right">3.29</td>
    <td align="right">3.23</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.23</td>
    <td align="right">2.68</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.13</td>
    <td align="right">3.55</td>
    <td align="right">3.93</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.07</td>
    <td align="right">3.92</td>
    <td align="right">4.77</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.48</td>
    <td align="right">3.20</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.25</td>
    <td align="right">2.04</td>
    <td align="right">1.92</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.44</td>
    <td align="right">1.83</td>
    <td align="right">1.84</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.44</td>
    <td align="right">1.78</td>
    <td align="right">1.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.17</td>
    <td align="right">1.62</td>
    <td align="right">1.85</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.26</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.85</td>
    <td align="right">2.30</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.33</td>
    <td align="right">2.70</td>
    <td align="right">1.94</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.14</td>
    <td align="right">3.00</td>
    <td align="right">3.00</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.89</td>
    <td align="right">3.20</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.96</td>
    <td align="right">2.91</td>
    <td align="right">2.31</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.23</td>
    <td align="right">3.92</td>
    <td align="right">3.89</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.08</td>
    <td align="right">3.88</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">3.63</td>
    <td align="right">3.43</td>
    <td align="right">11.14</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.63</td>
    <td align="right">4.72</td>
    <td align="right">14.40</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">8.22</td>
    <td align="right">5.41</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">5.14</td>
    <td align="right">4.70</td>
    <td align="right">11.44</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">7.93</td>
    <td align="right">5.16</td>
    <td align="right">11.55</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">11.06</td>
    <td align="right">7.57</td>
    <td align="right">7.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.89</td>
    <td align="right">6.21</td>
    <td align="right">10.99</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">10.15</td>
    <td align="right">6.71</td>
    <td align="right">12.59</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.18</td>
    <td align="right">8.30</td>
    <td align="right">8.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">8.05</td>
    <td align="right">7.64</td>
    <td align="right">11.85</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">12.36</td>
    <td align="right">6.85</td>
    <td align="right">11.32</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.08</td>
    <td align="right">12.87</td>
    <td align="right">11.90</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.22</td>
    <td align="right">12.85</td>
    <td align="right">8.12</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.46</td>
    <td align="right">8.21</td>
    <td align="right">17.96</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">2.65</td>
    <td align="right">3.37</td>
    <td align="right">3.53</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.58</td>
    <td align="right">2.52</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">27.17</td>
    <td align="right">24.90</td>
    <td align="right">21.45</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.93</td>
    <td align="right">5.51</td>
    <td align="right">5.76</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.21</td>
    <td align="right">6.27</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">47.70</td>
    <td align="right">37.07</td>
    <td align="right">22.32</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">9.77</td>
    <td align="right">8.64</td>
    <td align="right">8.17</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.83</td>
    <td align="right">8.32</td>
    <td align="right">7.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.76</td>
    <td align="right">51.50</td>
    <td align="right">24.81</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.57</td>
    <td align="right">9.92</td>
    <td align="right">10.87</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.92</td>
    <td align="right">7.80</td>
    <td align="right">7.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.44</td>
    <td align="right">4.40</td>
    <td align="right">3.14</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.09</td>
    <td align="right">4.17</td>
    <td align="right">4.48</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.18</td>
    <td align="right">4.18</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.38</td>
    <td align="right">8.18</td>
    <td align="right">7.72</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">6.21</td>
    <td align="right">5.13</td>
    <td align="right">7.87</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.29</td>
    <td align="right">6.45</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">13.74</td>
    <td align="right">12.40</td>
    <td align="right">11.12</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">14.91</td>
    <td align="right">13.17</td>
    <td align="right">12.48</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.34</td>
    <td align="right">11.60</td>
    <td align="right">7.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">17.59</td>
    <td align="right">16.23</td>
    <td align="right">17.89</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">19.76</td>
    <td align="right">21.74</td>
    <td align="right">19.31</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">13.38</td>
    <td align="right">15.69</td>
    <td align="right">9.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.60</td>
    <td align="right">5.43</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.00</td>
    <td align="right">2.72</td>
    <td align="right">2.61</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.97</td>
    <td align="right">2.77</td>
    <td align="right">3.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.67</td>
    <td align="right">4.19</td>
    <td align="right">4.54</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.39</td>
    <td align="right">4.59</td>
    <td align="right">5.98</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">5.14</td>
    <td align="right">5.96</td>
    <td align="right">6.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">9.26</td>
    <td align="right">9.03</td>
    <td align="right">5.96</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">12.10</td>
    <td align="right">10.93</td>
    <td align="right">11.05</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">12.49</td>
    <td align="right">10.79</td>
    <td align="right">11.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">11.73</td>
    <td align="right">12.60</td>
    <td align="right">6.81</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.97</td>
    <td align="right">13.55</td>
    <td align="right">14.09</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.00</td>
    <td align="right">15.24</td>
    <td align="right">15.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">6.10</td>
    <td align="right">5.95</td>
    <td align="right">13.06</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.21</td>
    <td align="right">6.49</td>
    <td align="right">15.91</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">9.48</td>
    <td align="right">8.10</td>
    <td align="right">8.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">12.79</td>
    <td align="right">9.70</td>
    <td align="right">14.42</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">19.79</td>
    <td align="right">13.06</td>
    <td align="right">15.42</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.49</td>
    <td align="right">15.80</td>
    <td align="right">15.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">19.03</td>
    <td align="right">14.98</td>
    <td align="right">15.06</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">27.15</td>
    <td align="right">17.98</td>
    <td align="right">17.23</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">29.04</td>
    <td align="right">30.65</td>
    <td align="right">21.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">24.22</td>
    <td align="right">19.94</td>
    <td align="right">15.86</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">27.74</td>
    <td align="right">19.33</td>
    <td align="right">16.60</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">41.11</td>
    <td align="right">36.05</td>
    <td align="right">36.19</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.67</td>
    <td align="right">5.71</td>
    <td align="right">3.52</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.05</td>
    <td align="right">12.27</td>
    <td align="right">16.90</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.80</td>
    <td align="right">4.23</td>
    <td align="right">4.25</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.93</td>
    <td align="right">5.21</td>
    <td align="right">5.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.53</td>
    <td align="right">17.66</td>
    <td align="right">17.54</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.96</td>
    <td align="right">4.97</td>
    <td align="right">4.77</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.02</td>
    <td align="right">5.94</td>
    <td align="right">5.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.65</td>
    <td align="right">21.26</td>
    <td align="right">16.78</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.60</td>
    <td align="right">5.31</td>
    <td align="right">5.31</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.32</td>
    <td align="right">6.45</td>
    <td align="right">6.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.17</td>
    <td align="right">27.34</td>
    <td align="right">17.30</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.96</td>
    <td align="right">5.89</td>
    <td align="right">5.92</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.31</td>
    <td align="right">7.34</td>
    <td align="right">7.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.94</td>
    <td align="right">5.55</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.23</td>
    <td align="right">5.66</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.40</td>
    <td align="right">3.96</td>
    <td align="right">3.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.20</td>
    <td align="right">8.21</td>
    <td align="right">8.26</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.33</td>
    <td align="right">8.77</td>
    <td align="right">8.73</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.94</td>
    <td align="right">4.85</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.59</td>
    <td align="right">10.74</td>
    <td align="right">10.92</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.96</td>
    <td align="right">10.42</td>
    <td align="right">10.43</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.99</td>
    <td align="right">7.04</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">17.46</td>
    <td align="right">14.19</td>
    <td align="right">14.26</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.83</td>
    <td align="right">13.62</td>
    <td align="right">12.72</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.20</td>
    <td align="right">7.21</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.26</td>
    <td align="right">3.80</td>
    <td align="right">3.82</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.50</td>
    <td align="right">5.42</td>
    <td align="right">5.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.70</td>
    <td align="right">5.40</td>
    <td align="right">5.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.28</td>
    <td align="right">5.62</td>
    <td align="right">4.71</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.74</td>
    <td align="right">5.92</td>
    <td align="right">5.08</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">6.97</td>
    <td align="right">7.02</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.12</td>
    <td align="right">6.74</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.84</td>
    <td align="right">9.31</td>
    <td align="right">7.43</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.94</td>
    <td align="right">9.71</td>
    <td align="right">7.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.11</td>
    <td align="right">6.91</td>
    <td align="right">5.18</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.05</td>
    <td align="right">10.52</td>
    <td align="right">7.57</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.26</td>
    <td align="right">10.62</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.98</td>
    <td align="right">8.55</td>
    <td align="right">13.72</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.23</td>
    <td align="right">11.57</td>
    <td align="right">17.09</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">13.00</td>
    <td align="right">11.97</td>
    <td align="right">12.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">12.10</td>
    <td align="right">11.79</td>
    <td align="right">14.47</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">14.05</td>
    <td align="right">13.61</td>
    <td align="right">16.03</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">19.13</td>
    <td align="right">17.89</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.47</td>
    <td align="right">14.69</td>
    <td align="right">14.43</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">18.53</td>
    <td align="right">17.25</td>
    <td align="right">15.53</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">21.66</td>
    <td align="right">19.38</td>
    <td align="right">19.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.09</td>
    <td align="right">17.43</td>
    <td align="right">15.28</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">21.34</td>
    <td align="right">20.42</td>
    <td align="right">15.00</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">30.00</td>
    <td align="right">28.58</td>
    <td align="right">28.24</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.70</td>
    <td align="right">22.36</td>
    <td align="right">9.18</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.50</td>
    <td align="right">12.97</td>
    <td align="right">17.61</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.97</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.94</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">22.26</td>
    <td align="right">19.00</td>
    <td align="right">18.39</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.67</td>
    <td align="right">5.10</td>
    <td align="right">5.30</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.32</td>
    <td align="right">6.42</td>
    <td align="right">6.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">28.63</td>
    <td align="right">24.90</td>
    <td align="right">18.20</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.22</td>
    <td align="right">5.85</td>
    <td align="right">5.84</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">10.83</td>
    <td align="right">7.46</td>
    <td align="right">7.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">51.31</td>
    <td align="right">45.13</td>
    <td align="right">19.62</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">15.02</td>
    <td align="right">8.87</td>
    <td align="right">8.62</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">16.07</td>
    <td align="right">11.77</td>
    <td align="right">11.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.38</td>
    <td align="right">6.20</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.54</td>
    <td align="right">6.25</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.75</td>
    <td align="right">4.14</td>
    <td align="right">4.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">17.55</td>
    <td align="right">10.31</td>
    <td align="right">10.16</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">20.23</td>
    <td align="right">9.26</td>
    <td align="right">9.30</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.31</td>
    <td align="right">5.29</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">21.32</td>
    <td align="right">14.30</td>
    <td align="right">13.41</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">28.70</td>
    <td align="right">15.99</td>
    <td align="right">12.28</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.45</td>
    <td align="right">8.83</td>
    <td align="right">6.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.30</td>
    <td align="right">20.26</td>
    <td align="right">20.79</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">25.87</td>
    <td align="right">17.83</td>
    <td align="right">17.75</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">10.66</td>
    <td align="right">13.35</td>
    <td align="right">14.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.59</td>
    <td align="right">4.24</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.04</td>
    <td align="right">5.92</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.15</td>
    <td align="right">5.72</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.79</td>
    <td align="right">6.22</td>
    <td align="right">5.38</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.35</td>
    <td align="right">6.40</td>
    <td align="right">5.42</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">7.59</td>
    <td align="right">7.56</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.20</td>
    <td align="right">7.98</td>
    <td align="right">5.83</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">11.00</td>
    <td align="right">10.41</td>
    <td align="right">8.28</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.25</td>
    <td align="right">10.75</td>
    <td align="right">8.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">8.58</td>
    <td align="right">10.94</td>
    <td align="right">8.89</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">15.55</td>
    <td align="right">16.12</td>
    <td align="right">12.03</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.39</td>
    <td align="right">13.81</td>
    <td align="right">9.69</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">10.01</td>
    <td align="right">9.56</td>
    <td align="right">13.99</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.78</td>
    <td align="right">12.66</td>
    <td align="right">17.63</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">16.84</td>
    <td align="right">15.02</td>
    <td align="right">15.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">13.99</td>
    <td align="right">12.98</td>
    <td align="right">15.01</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.23</td>
    <td align="right">14.95</td>
    <td align="right">16.83</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">23.43</td>
    <td align="right">21.66</td>
    <td align="right">22.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">17.30</td>
    <td align="right">17.33</td>
    <td align="right">15.94</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">24.04</td>
    <td align="right">22.49</td>
    <td align="right">17.79</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">26.69</td>
    <td align="right">23.19</td>
    <td align="right">24.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">27.40</td>
    <td align="right">24.81</td>
    <td align="right">18.53</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">33.79</td>
    <td align="right">33.16</td>
    <td align="right">18.27</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">40.48</td>
    <td align="right">39.28</td>
    <td align="right">37.92</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.17</td>
    <td align="right">31.93</td>
    <td align="right">16.79</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.11</td>
    <td align="right">41.74</td>
    <td align="right">36.39</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.35</td>
    <td align="right">15.45</td>
    <td align="right">15.41</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.05</td>
    <td align="right">19.16</td>
    <td align="right">19.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">36.56</td>
    <td align="right">63.03</td>
    <td align="right">38.49</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.26</td>
    <td align="right">19.59</td>
    <td align="right">19.57</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">15.94</td>
    <td align="right">18.62</td>
    <td align="right">18.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.22</td>
    <td align="right">77.42</td>
    <td align="right">38.06</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.31</td>
    <td align="right">18.50</td>
    <td align="right">18.41</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.03</td>
    <td align="right">18.20</td>
    <td align="right">18.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">55.70</td>
    <td align="right">95.73</td>
    <td align="right">37.78</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.07</td>
    <td align="right">18.79</td>
    <td align="right">18.71</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.52</td>
    <td align="right">19.51</td>
    <td align="right">19.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.17</td>
    <td align="right">21.13</td>
    <td align="right">21.18</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.23</td>
    <td align="right">22.16</td>
    <td align="right">22.10</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.90</td>
    <td align="right">13.58</td>
    <td align="right">13.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">20.69</td>
    <td align="right">25.87</td>
    <td align="right">25.87</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.31</td>
    <td align="right">27.39</td>
    <td align="right">27.51</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.83</td>
    <td align="right">15.77</td>
    <td align="right">15.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.81</td>
    <td align="right">33.15</td>
    <td align="right">33.16</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.32</td>
    <td align="right">46.28</td>
    <td align="right">45.85</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.70</td>
    <td align="right">19.34</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.05</td>
    <td align="right">35.45</td>
    <td align="right">35.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.30</td>
    <td align="right">56.04</td>
    <td align="right">56.25</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.28</td>
    <td align="right">25.44</td>
    <td align="right">25.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.42</td>
    <td align="right">15.57</td>
    <td align="right">15.53</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.17</td>
    <td align="right">21.23</td>
    <td align="right">20.75</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.45</td>
    <td align="right">22.16</td>
    <td align="right">22.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.93</td>
    <td align="right">20.40</td>
    <td align="right">20.45</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">20.81</td>
    <td align="right">25.87</td>
    <td align="right">25.92</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.30</td>
    <td align="right">27.58</td>
    <td align="right">27.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.06</td>
    <td align="right">24.66</td>
    <td align="right">24.69</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.15</td>
    <td align="right">33.18</td>
    <td align="right">33.17</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.25</td>
    <td align="right">46.53</td>
    <td align="right">45.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.03</td>
    <td align="right">36.13</td>
    <td align="right">36.90</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.17</td>
    <td align="right">35.85</td>
    <td align="right">35.85</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.65</td>
    <td align="right">56.33</td>
    <td align="right">56.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.05</td>
    <td align="right">20.69</td>
    <td align="right">25.32</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">30.91</td>
    <td align="right">29.23</td>
    <td align="right">34.30</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.07</td>
    <td align="right">29.97</td>
    <td align="right">29.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.23</td>
    <td align="right">27.91</td>
    <td align="right">25.51</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.22</td>
    <td align="right">33.87</td>
    <td align="right">32.56</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">37.42</td>
    <td align="right">38.31</td>
    <td align="right">38.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.33</td>
    <td align="right">33.36</td>
    <td align="right">25.79</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">46.60</td>
    <td align="right">41.17</td>
    <td align="right">33.97</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.06</td>
    <td align="right">40.93</td>
    <td align="right">41.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.41</td>
    <td align="right">39.84</td>
    <td align="right">26.88</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.17</td>
    <td align="right">43.23</td>
    <td align="right">31.48</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">53.75</td>
    <td align="right">57.85</td>
    <td align="right">58.23</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.74</td>
    <td align="right">109.02</td>
    <td align="right">19.22</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">27.49</td>
    <td align="right">42.70</td>
    <td align="right">39.22</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.81</td>
    <td align="right">15.53</td>
    <td align="right">15.64</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.28</td>
    <td align="right">19.26</td>
    <td align="right">19.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.98</td>
    <td align="right">63.07</td>
    <td align="right">41.26</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">18.45</td>
    <td align="right">21.21</td>
    <td align="right">21.42</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.76</td>
    <td align="right">20.81</td>
    <td align="right">20.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">50.89</td>
    <td align="right">125.14</td>
    <td align="right">59.87</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">30.63</td>
    <td align="right">31.38</td>
    <td align="right">28.63</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">28.16</td>
    <td align="right">23.63</td>
    <td align="right">25.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">105.67</td>
    <td align="right">134.65</td>
    <td align="right">51.11</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">27.70</td>
    <td align="right">28.79</td>
    <td align="right">30.71</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">30.76</td>
    <td align="right">31.24</td>
    <td align="right">30.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.47</td>
    <td align="right">21.60</td>
    <td align="right">21.58</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.82</td>
    <td align="right">23.35</td>
    <td align="right">23.16</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">10.91</td>
    <td align="right">13.71</td>
    <td align="right">13.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.07</td>
    <td align="right">26.53</td>
    <td align="right">27.12</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">46.36</td>
    <td align="right">30.15</td>
    <td align="right">30.45</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">13.06</td>
    <td align="right">15.94</td>
    <td align="right">16.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">37.61</td>
    <td align="right">49.32</td>
    <td align="right">50.00</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.48</td>
    <td align="right">63.83</td>
    <td align="right">51.58</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">17.97</td>
    <td align="right">23.63</td>
    <td align="right">24.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">54.51</td>
    <td align="right">64.15</td>
    <td align="right">68.08</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">99.64</td>
    <td align="right">71.02</td>
    <td align="right">70.88</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">34.05</td>
    <td align="right">51.94</td>
    <td align="right">50.94</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.70</td>
    <td align="right">15.75</td>
    <td align="right">15.84</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.47</td>
    <td align="right">21.68</td>
    <td align="right">21.69</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.99</td>
    <td align="right">23.04</td>
    <td align="right">22.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">20.82</td>
    <td align="right">24.23</td>
    <td align="right">23.26</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">22.60</td>
    <td align="right">29.05</td>
    <td align="right">35.12</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">75.91</td>
    <td align="right">31.89</td>
    <td align="right">32.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.60</td>
    <td align="right">40.96</td>
    <td align="right">45.90</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">41.67</td>
    <td align="right">40.14</td>
    <td align="right">45.16</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.54</td>
    <td align="right">63.61</td>
    <td align="right">50.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">64.00</td>
    <td align="right">73.69</td>
    <td align="right">68.18</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.42</td>
    <td align="right">57.31</td>
    <td align="right">60.60</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">96.84</td>
    <td align="right">70.91</td>
    <td align="right">70.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.36</td>
    <td align="right">21.16</td>
    <td align="right">26.24</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.22</td>
    <td align="right">29.49</td>
    <td align="right">35.72</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">28.89</td>
    <td align="right">32.17</td>
    <td align="right">32.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">27.75</td>
    <td align="right">28.53</td>
    <td align="right">26.09</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">43.89</td>
    <td align="right">40.46</td>
    <td align="right">36.76</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">39.26</td>
    <td align="right">40.24</td>
    <td align="right">40.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">53.86</td>
    <td align="right">51.20</td>
    <td align="right">39.79</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">96.13</td>
    <td align="right">84.49</td>
    <td align="right">51.24</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">44.56</td>
    <td align="right">45.62</td>
    <td align="right">53.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">98.67</td>
    <td align="right">96.69</td>
    <td align="right">51.22</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">117.90</td>
    <td align="right">118.13</td>
    <td align="right">71.48</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">81.56</td>
    <td align="right">101.05</td>
    <td align="right">111.33</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.09</td>
    <td align="right">10.07</td>
    <td align="right">6.85</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">13.88</td>
    <td align="right">22.90</td>
    <td align="right">26.71</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.57</td>
    <td align="right">12.39</td>
    <td align="right">12.39</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.75</td>
    <td align="right">13.88</td>
    <td align="right">13.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.56</td>
    <td align="right">35.28</td>
    <td align="right">28.80</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">12.05</td>
    <td align="right">14.06</td>
    <td align="right">14.10</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.50</td>
    <td align="right">15.33</td>
    <td align="right">15.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.91</td>
    <td align="right">47.51</td>
    <td align="right">30.25</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.77</td>
    <td align="right">15.40</td>
    <td align="right">15.46</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.69</td>
    <td align="right">16.74</td>
    <td align="right">16.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.05</td>
    <td align="right">60.36</td>
    <td align="right">30.91</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.57</td>
    <td align="right">16.28</td>
    <td align="right">16.27</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.93</td>
    <td align="right">17.81</td>
    <td align="right">18.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.65</td>
    <td align="right">16.13</td>
    <td align="right">16.14</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.26</td>
    <td align="right">16.73</td>
    <td align="right">16.76</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.12</td>
    <td align="right">9.36</td>
    <td align="right">9.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.35</td>
    <td align="right">22.44</td>
    <td align="right">22.45</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.33</td>
    <td align="right">22.40</td>
    <td align="right">22.36</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.14</td>
    <td align="right">13.94</td>
    <td align="right">13.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.30</td>
    <td align="right">32.32</td>
    <td align="right">32.58</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.90</td>
    <td align="right">30.83</td>
    <td align="right">30.83</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.44</td>
    <td align="right">17.63</td>
    <td align="right">17.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.06</td>
    <td align="right">36.01</td>
    <td align="right">35.95</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.50</td>
    <td align="right">36.23</td>
    <td align="right">35.97</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.49</td>
    <td align="right">20.54</td>
    <td align="right">20.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.63</td>
    <td align="right">9.45</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.75</td>
    <td align="right">16.22</td>
    <td align="right">16.23</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.33</td>
    <td align="right">16.82</td>
    <td align="right">16.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.75</td>
    <td align="right">13.76</td>
    <td align="right">13.75</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.48</td>
    <td align="right">22.50</td>
    <td align="right">22.52</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">18.43</td>
    <td align="right">22.32</td>
    <td align="right">22.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.93</td>
    <td align="right">17.65</td>
    <td align="right">17.70</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.16</td>
    <td align="right">32.38</td>
    <td align="right">32.36</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.89</td>
    <td align="right">30.80</td>
    <td align="right">30.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.14</td>
    <td align="right">20.95</td>
    <td align="right">20.86</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">27.22</td>
    <td align="right">35.96</td>
    <td align="right">36.00</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.17</td>
    <td align="right">35.97</td>
    <td align="right">35.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.42</td>
    <td align="right">16.54</td>
    <td align="right">20.00</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">49.20</td>
    <td align="right">33.08</td>
    <td align="right">36.97</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.63</td>
    <td align="right">24.07</td>
    <td align="right">23.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.00</td>
    <td align="right">23.70</td>
    <td align="right">20.75</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.67</td>
    <td align="right">37.41</td>
    <td align="right">35.63</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.27</td>
    <td align="right">31.84</td>
    <td align="right">31.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">24.18</td>
    <td align="right">30.61</td>
    <td align="right">20.39</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.72</td>
    <td align="right">44.39</td>
    <td align="right">36.26</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.49</td>
    <td align="right">35.26</td>
    <td align="right">35.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">30.26</td>
    <td align="right">38.96</td>
    <td align="right">25.11</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">64.24</td>
    <td align="right">50.74</td>
    <td align="right">38.93</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">42.12</td>
    <td align="right">45.72</td>
    <td align="right">45.94</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.46</td>
    <td align="right">43.56</td>
    <td align="right">10.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.09</td>
    <td align="right">22.79</td>
    <td align="right">28.31</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.73</td>
    <td align="right">12.62</td>
    <td align="right">12.63</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">12.01</td>
    <td align="right">14.05</td>
    <td align="right">14.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.77</td>
    <td align="right">35.08</td>
    <td align="right">29.73</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">14.00</td>
    <td align="right">14.27</td>
    <td align="right">14.57</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.44</td>
    <td align="right">15.33</td>
    <td align="right">15.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">27.43</td>
    <td align="right">49.58</td>
    <td align="right">34.91</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">23.74</td>
    <td align="right">16.52</td>
    <td align="right">15.91</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">15.40</td>
    <td align="right">16.97</td>
    <td align="right">17.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">38.52</td>
    <td align="right">68.08</td>
    <td align="right">35.30</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">24.71</td>
    <td align="right">18.64</td>
    <td align="right">20.93</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">32.82</td>
    <td align="right">37.37</td>
    <td align="right">32.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.13</td>
    <td align="right">16.73</td>
    <td align="right">16.70</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.38</td>
    <td align="right">17.51</td>
    <td align="right">17.55</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.31</td>
    <td align="right">9.50</td>
    <td align="right">9.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.36</td>
    <td align="right">22.24</td>
    <td align="right">22.55</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">20.05</td>
    <td align="right">23.33</td>
    <td align="right">22.53</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.40</td>
    <td align="right">14.40</td>
    <td align="right">15.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">30.21</td>
    <td align="right">39.68</td>
    <td align="right">36.97</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">28.72</td>
    <td align="right">33.00</td>
    <td align="right">42.49</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">20.60</td>
    <td align="right">21.22</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">58.38</td>
    <td align="right">37.96</td>
    <td align="right">42.44</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">40.81</td>
    <td align="right">63.96</td>
    <td align="right">41.35</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">21.16</td>
    <td align="right">25.21</td>
    <td align="right">25.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.79</td>
    <td align="right">9.61</td>
    <td align="right">9.61</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.12</td>
    <td align="right">16.75</td>
    <td align="right">16.74</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.37</td>
    <td align="right">17.56</td>
    <td align="right">17.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.83</td>
    <td align="right">13.49</td>
    <td align="right">13.46</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">17.06</td>
    <td align="right">21.98</td>
    <td align="right">21.95</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">18.53</td>
    <td align="right">22.19</td>
    <td align="right">22.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">13.25</td>
    <td align="right">17.90</td>
    <td align="right">17.84</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.72</td>
    <td align="right">44.86</td>
    <td align="right">48.98</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">27.85</td>
    <td align="right">32.10</td>
    <td align="right">34.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">18.82</td>
    <td align="right">27.86</td>
    <td align="right">23.38</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">57.04</td>
    <td align="right">77.27</td>
    <td align="right">65.64</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">43.75</td>
    <td align="right">45.37</td>
    <td align="right">72.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.60</td>
    <td align="right">16.92</td>
    <td align="right">20.60</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">51.65</td>
    <td align="right">34.44</td>
    <td align="right">38.58</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">23.18</td>
    <td align="right">26.02</td>
    <td align="right">26.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">21.58</td>
    <td align="right">25.89</td>
    <td align="right">22.68</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">85.85</td>
    <td align="right">73.69</td>
    <td align="right">54.17</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">32.36</td>
    <td align="right">34.52</td>
    <td align="right">34.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">36.75</td>
    <td align="right">55.36</td>
    <td align="right">27.37</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">110.37</td>
    <td align="right">102.41</td>
    <td align="right">62.36</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">35.74</td>
    <td align="right">38.37</td>
    <td align="right">46.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">70.95</td>
    <td align="right">92.40</td>
    <td align="right">44.11</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">132.39</td>
    <td align="right">102.93</td>
    <td align="right">71.48</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">52.78</td>
    <td align="right">53.67</td>
    <td align="right">53.61</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.20</td>
    <td align="right">8.46</td>
    <td align="right">6.59</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.00</td>
    <td align="right">54.64</td>
    <td align="right">41.47</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.75</td>
    <td align="right">20.36</td>
    <td align="right">24.33</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">25.37</td>
    <td align="right">25.94</td>
    <td align="right">29.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.13</td>
    <td align="right">80.03</td>
    <td align="right">44.03</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.95</td>
    <td align="right">21.92</td>
    <td align="right">24.01</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">27.26</td>
    <td align="right">28.43</td>
    <td align="right">30.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">109.66</td>
    <td align="right">97.35</td>
    <td align="right">42.91</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.23</td>
    <td align="right">22.74</td>
    <td align="right">24.19</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">29.42</td>
    <td align="right">30.95</td>
    <td align="right">31.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.83</td>
    <td align="right">122.50</td>
    <td align="right">44.90</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.27</td>
    <td align="right">24.20</td>
    <td align="right">25.12</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.88</td>
    <td align="right">34.09</td>
    <td align="right">33.78</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">23.40</td>
    <td align="right">43.02</td>
    <td align="right">43.59</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">27.36</td>
    <td align="right">43.02</td>
    <td align="right">43.31</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.65</td>
    <td align="right">24.64</td>
    <td align="right">24.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">28.06</td>
    <td align="right">58.17</td>
    <td align="right">58.71</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.41</td>
    <td align="right">59.55</td>
    <td align="right">59.11</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.42</td>
    <td align="right">36.24</td>
    <td align="right">25.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">39.82</td>
    <td align="right">79.75</td>
    <td align="right">80.25</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.77</td>
    <td align="right">80.41</td>
    <td align="right">80.25</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.91</td>
    <td align="right">54.65</td>
    <td align="right">39.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">44.05</td>
    <td align="right">88.32</td>
    <td align="right">88.42</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">51.76</td>
    <td align="right">95.40</td>
    <td align="right">96.35</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">28.94</td>
    <td align="right">55.59</td>
    <td align="right">40.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.51</td>
    <td align="right">25.83</td>
    <td align="right">25.75</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.67</td>
    <td align="right">29.13</td>
    <td align="right">29.17</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.78</td>
    <td align="right">30.67</td>
    <td align="right">30.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">19.14</td>
    <td align="right">46.64</td>
    <td align="right">34.83</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.39</td>
    <td align="right">39.87</td>
    <td align="right">27.41</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.03</td>
    <td align="right">51.66</td>
    <td align="right">40.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.68</td>
    <td align="right">54.23</td>
    <td align="right">38.95</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">32.87</td>
    <td align="right">52.73</td>
    <td align="right">34.94</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.36</td>
    <td align="right">60.88</td>
    <td align="right">43.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.67</td>
    <td align="right">55.19</td>
    <td align="right">39.14</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.62</td>
    <td align="right">63.88</td>
    <td align="right">44.21</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.21</td>
    <td align="right">63.71</td>
    <td align="right">44.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.71</td>
    <td align="right">43.55</td>
    <td align="right">35.81</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">32.06</td>
    <td align="right">55.58</td>
    <td align="right">41.87</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">36.66</td>
    <td align="right">62.33</td>
    <td align="right">62.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.72</td>
    <td align="right">60.86</td>
    <td align="right">36.75</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.46</td>
    <td align="right">64.04</td>
    <td align="right">39.49</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">44.82</td>
    <td align="right">80.51</td>
    <td align="right">80.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.73</td>
    <td align="right">73.42</td>
    <td align="right">36.82</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">48.60</td>
    <td align="right">80.37</td>
    <td align="right">41.59</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.13</td>
    <td align="right">87.11</td>
    <td align="right">87.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">51.34</td>
    <td align="right">93.84</td>
    <td align="right">38.27</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.42</td>
    <td align="right">97.45</td>
    <td align="right">40.97</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">66.80</td>
    <td align="right">125.21</td>
    <td align="right">125.02</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">59.75</td>
    <td align="right">36.05</td>
    <td align="right">11.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">66.45</td>
    <td align="right">59.52</td>
    <td align="right">46.18</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.22</td>
    <td align="right">21.53</td>
    <td align="right">26.43</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">28.24</td>
    <td align="right">28.97</td>
    <td align="right">33.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">97.67</td>
    <td align="right">85.47</td>
    <td align="right">47.41</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">25.86</td>
    <td align="right">23.00</td>
    <td align="right">25.46</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">31.08</td>
    <td align="right">30.98</td>
    <td align="right">34.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">124.71</td>
    <td align="right">110.11</td>
    <td align="right">47.34</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">28.25</td>
    <td align="right">24.37</td>
    <td align="right">26.17</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">34.59</td>
    <td align="right">35.20</td>
    <td align="right">36.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">185.95</td>
    <td align="right">168.28</td>
    <td align="right">53.54</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">36.10</td>
    <td align="right">29.99</td>
    <td align="right">29.97</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">39.69</td>
    <td align="right">41.69</td>
    <td align="right">41.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.42</td>
    <td align="right">43.81</td>
    <td align="right">44.22</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">29.90</td>
    <td align="right">44.51</td>
    <td align="right">43.99</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.75</td>
    <td align="right">29.04</td>
    <td align="right">29.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.17</td>
    <td align="right">58.90</td>
    <td align="right">59.71</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.24</td>
    <td align="right">62.29</td>
    <td align="right">61.59</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">19.06</td>
    <td align="right">41.54</td>
    <td align="right">29.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.89</td>
    <td align="right">82.98</td>
    <td align="right">83.38</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">48.98</td>
    <td align="right">82.16</td>
    <td align="right">82.88</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">32.65</td>
    <td align="right">63.95</td>
    <td align="right">46.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">49.91</td>
    <td align="right">93.52</td>
    <td align="right">93.62</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">59.41</td>
    <td align="right">106.43</td>
    <td align="right">105.04</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">44.93</td>
    <td align="right">76.61</td>
    <td align="right">58.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.69</td>
    <td align="right">30.88</td>
    <td align="right">30.69</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.73</td>
    <td align="right">33.09</td>
    <td align="right">33.05</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.86</td>
    <td align="right">35.37</td>
    <td align="right">35.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.69</td>
    <td align="right">52.71</td>
    <td align="right">40.53</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.43</td>
    <td align="right">42.39</td>
    <td align="right">30.42</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.28</td>
    <td align="right">57.31</td>
    <td align="right">44.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">33.91</td>
    <td align="right">64.83</td>
    <td align="right">49.68</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">35.74</td>
    <td align="right">60.45</td>
    <td align="right">40.42</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">33.53</td>
    <td align="right">66.94</td>
    <td align="right">48.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">42.67</td>
    <td align="right">72.24</td>
    <td align="right">58.68</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">42.22</td>
    <td align="right">77.22</td>
    <td align="right">54.26</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">40.21</td>
    <td align="right">78.07</td>
    <td align="right">57.33</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.84</td>
    <td align="right">44.47</td>
    <td align="right">39.35</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">36.61</td>
    <td align="right">56.72</td>
    <td align="right">45.77</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.67</td>
    <td align="right">63.36</td>
    <td align="right">63.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">39.97</td>
    <td align="right">62.52</td>
    <td align="right">39.62</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">46.60</td>
    <td align="right">67.22</td>
    <td align="right">43.20</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">47.61</td>
    <td align="right">81.70</td>
    <td align="right">81.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">47.50</td>
    <td align="right">78.76</td>
    <td align="right">41.58</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">58.12</td>
    <td align="right">89.65</td>
    <td align="right">48.89</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">52.84</td>
    <td align="right">88.99</td>
    <td align="right">90.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">64.94</td>
    <td align="right">109.71</td>
    <td align="right">46.85</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">83.13</td>
    <td align="right">122.13</td>
    <td align="right">55.17</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">75.05</td>
    <td align="right">131.82</td>
    <td align="right">132.37</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
